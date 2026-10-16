---
layout: post
title:  "Manifolds for Five-Year Olds"
date:   2026-10-12 00:58:57 -0400
categories: writing
excerpt: "Mechinterp jargon like featurizers, SAEs and block sparsity, explained so simply a five-year-old could follow."
---

Ambitious mechanistic interpretability research is full of jargon, but the underlying intuitions are so simple that a five-year-old (with a firm grasp of linear algebra) could understand them.

In one [recent paper](https://www.goodfire.com/research/bsf-vision#) from Goodfire, the authors declare that "block sparsity is the inductive bias matched to a generative process in which each representation is a sparse sum of low-dimensional manifolds." Then they implement

> ...three variants of block-sparse featurizers (BSFs) and, through a minimum-description-length analysis, show that all three describe activations more compactly than direction-based featurizers, with the recovered concepts typically two- to four-dimensional.

In simple terms, they create a new method to translate a model's neural activations into intelligible concepts. Its core idea is that related concepts are arranged close together in the model's mind, so to speak, in arrangements that mimic the intuitive relationships between those concepts. The paper's Minkowski sums, Stiefel manifolds, ω-fold periodic Fourier modes, and Claude-y neologisms all center on this intuition.

By the paper's measures, this method works better than "sparse autoencoders" (SAEs), which suggests that its underlying intuition provides a better understanding of how models internally relate concepts than the intuition behind SAEs.

Now, what did all those strange words mean? And what does this have to do with manifolds?

### 1\. What is a "featurizer"?

**Big Idea:** We can transform and combine the values in an activation vector to get values that are more meaningful than the raw ones.

In the mechinterp context, a featurizer is an algorithm or neural network that takes an activation vector and turns it into a bunch of "features". In machine learning jargon, features are functions of the input data.

Sometimes features are a lot more useful and intuitive than the raw data. For example, say we have a bunch of data points for a toy car moving along a track at a 30° angle relative to the x and y axis. We can take a weighted sum of the x and y distance to get a single "distance along the track" metric for each point in time, which is more meaningful than the raw x and y values.

### 2\. What is a "sparse autoencoder" (SAE)?

**Big Idea:** A sparse autoencoder is a featurizer intended to make feature represent a distinct concept. Then it can take in an activation vector and reveal the concepts it represents.

**Big Idea:** SAEs assume that each activation vector corresponds to only a few concepts.

**Big Idea:** SAEs assume that there is a direction in activation space corresponding to each distinct concept.

If all of a model's internal "thoughts" can be expressed in activation space[^1], we might guess that there is some meaningful structure to this space. For example, two similar thoughts would correspond to activation vectors that are "close" in some sense; two thoughts that contain the same concept would correspond to activation vectors that are "similar" in some sense.

However, the model is trained to be good at predicting text (or being an assistant); the way it uses activation space is the result of aggressive optimization pressure on its output. There's no reason activation vectors should be easy to interpret, and they aren't.

But, if there is structure, structure can be used to compress information! That gives us an objective at which to target deep learning if we want to uncover the structure. We can train a neural network (or encoder) to compress an activation vector into a new representation and train a second network (or decoder) to decompress it back into an activation vector, with the objective being to make the reconstruction as accurate as possible. The learning process will naturally rediscover this structure to make good, concise descriptions of the activations. (This kind of model, which learns how to translate into and out of a compressed format, is called an "autoencoder".)

Can we force the compression format to be easily interpretable? One way to do this is to assume that each thought involves a few distinct concepts. There is an enormous amount of concepts in total, so our compressed representation should have tons of different slots for concepts, but each activation should only light up the small number of concepts that the thought is about. (Hence, the feature vector is "sparse": most of the entries should be zero most of the time.) We can incorporate a penalty into our autoencoder training loss to enforce this.

Once we train this "sparse autoencoder", how can we tell what concept each slot represents? We can feed a ton of sample text into the models and track which features they light up. When we (or a bunch of LLMs) review the results, and we see that all the text samples that light up Feature 1 obviously share some concept, we know that Feature 1 represents that concept. If a lot of our features seem obviously meaningful in this way, then we have something useful.

In the original SAE architecture, each feature is a linear combination of the activations at a given layer.[^2] What assumption does this come with? It means that for every concept, there is a corresponding line in the activation space, and the further you go along this line, the more concept-y the activation is. There is a line corresponding to "Golden Gate bridge", and if the model is thinking of the Golden Gate Bridge than the activation will point strongly in the direction of the "Golden Gate Bridge" line.

Considering the rigidity of their assumptions, SAEs work surprisingly well at finding coherent concepts, and some of them can even be added to the activations to steer models towards these concepts (e.g. Golden Gate Claude). SAEs even provide some notion of similarity between concepts: the features that are closest in direction represent similar concepts (e.g., Alcatraz and other San Francisco locations were among the closest to the Golden Gate Bridge feature).

But there are some distinct concepts we expect to lie along the *same* line, like temperatures from "burning" to "hot" to "cold" to "freezing". Others might lie along a ring, like the days of the week, which proceed in order but then loop around again. Yet others might be related in multiple dimensions, like countries on a 2D map. Can find a way to relate concepts more generally than measuring the angle between the concept-lines?

### 5\. What is a "manifold"?

**Big Idea:** We can spatially represent groups of related concepts in shapes called manifolds.

Say someone gave you a ton of points and told you to arrange them way you want, in however many dimensions, with only one condition: you should be able to take a walk along the resulting shape from any point to any other point. Also, the amount of (orthogonal) directions you can walk in should be the same at any one of the points. What are some shapes that satisfy this? A line, a curve, a plane, a wavy plane, a sphere, and a torus all do.

These are all manifolds. A manifold is just an object that looks like a hyperplane up close. A curve in space just looks like a line if you zoom in to it enough; a sphere looks like a flat plane if you zoom in enough.

So, if a bunch of concepts are all related to each other, and you express that similarity as adjacency in space, the spatial representation of that is a manifold. The main feature of a manifold is that you can travel smoothly along it, and the same must hold for your concepts. They must be related in a way where you can go from one to the next: from Monday to Friday, from hot to cold, from red to green to blue.

The manifold assumption excludes shapes like plus signs, where there is some special intersection concept from which one could move along two different axes, whereas at all other concepts you can only move along one axis. Under the manifold assumption, some spatial structure unifies the concepts: from any location on the earth, I can move on the north-south axis or the east-west axis; from any day in the month of February, I can move along the time axis.[^3]

### 6\. What is a "block-sparse featurizer" (BSF)?

**Big Idea:** BSFs group features together into blocks. For each block, the features become the coordinate axes of a low-dimensional space, which is meant to hold a manifold.

**Big Idea:** In BSFs, a concept is a vector pointing to part of a manifold. The manifold is kind of like a concept-web. Within each manifold, the concepts are related in interpretable ways. Different manifolds are generally unrelated.

**Big Idea:** Like SAEs, BSFs assume that each activation vector corresponds to only a few concepts (this kind of assumption seems necessary to make these interpretability methods interpretable at all), but this time each concept is a vector from a distinct manifold.

Block-sparse featurizers (BSFs) are similar to SAEs in that they translate an activation vector into features, each of which is a linear combination of the activations, and then try to reconstruct the activation vector. However, the BSF features are grouped into "blocks", and learn as blocks. The BSF learns to use its blocks to represent distinct blobs of concepts.

The sparsity pressure is applied over the blocks, rather than the individual features: for any input, only a few blocks should be activated. Hence, they are "block-sparse". On the other hand, an activated block can use or ignore as many of its features as its wants with no penalty.

The two types of featurizers are hard to compare apples-to-apples, since the work a feature does in a BSF is different from the work a feature does in a BSF. The authors come up with a method ("minimum-description-length analysis") to compare how many bits it takes to reconstruct an activation accurately using the BSF representation one versus the SAE one. The BSFs win, and this suggests that they leverage the structure of activation vectors better than SAEs.

After training the BSFs, the authors figure out what some of the resulting manifolds represent, and there are some visually interesting results on the post. But it's clear that, like with SAEs, finding clear meaning in the blocks isn't easy; most of them aren't obviously meaningful.

### Sources

1. [Toy Models of Superposition](https://transformer-circuits.pub/2022/toy_model)
2. [Scaling Monosemanticity: Extracting Interpretable Features from Claude 3 Sonnet](https://transformer-circuits.pub/2024/scaling-monosemanticity/)
3. [Structuring Sparsity: Block-Sparse Featurizers Capture Visual Concept Manifolds](https://www.goodfire.com/research/bsf-vision#)

*Originally posted on [LessWrong](https://www.lesswrong.com/posts/SwR9hFLn2DLbZZfD9/manifolds-for-five-year-olds).*
{: .post-crosspost}

[^1]: When you run a neural network, each layer produces a number at each neuron, which we all an "activation". Therefore we can speak of an "activation vector", which is all the activation numbers at a given layer listed in neuron order, and "activation space", a multidimensional space which contains all the possible activation vectors.

[^2]: There is a nonlinear function applied after the encoder's linear transformation. But this is a ReLU function, which just makes negative numbers zero, so the intuition remains similar. Basically, if an activation vector projects onto the negative part of the "blue" line, rather than being "negative blue" we just zero it and treat it as "not blue".

[^3]: We're also assuming that most of our concepts can meaningfully be spatially related in the first place. We can't have two concepts can both be close to a third but extraordinarily far apart from each other.
