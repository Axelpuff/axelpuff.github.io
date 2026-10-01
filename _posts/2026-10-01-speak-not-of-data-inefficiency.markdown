---
layout: post
title:  "Speak Not of Data Inefficiency"
date:   2026-10-01 02:07:37 -0400
categories: writing
excerpt: "A preschooler has seen petabytes of video and runs on trillions of parameters. Are language models really the data-inefficient ones?"
---

Humans are really bad at comparing themselves to models.

Take, for example, Leopold's preschooler graph:

![Leopold Aschenbrenner's "Base Scaleup of Effective Compute" graph, placing GPT-2 at preschooler, GPT-3 at elementary schooler, and GPT-4 at smart high schooler level]({{ '/assets/posts/speak-not-of-data-inefficiency/s17itspaufzfpfqf0k8x.png' | relative_url }})

Set aside, for a moment, concerns of scaling and RSI, and meditate: what characteristics does GPT-2 share with a preschooler?

- Rudimentary control of human language
- The ability to count the R's in "strawberry" incorrectly
- ...

I can't come up with anything else, because these two entities are almost completely disjoint. Is GPT-2 capable of bipedal locomotion, recognizing its mother's voice, or naming people by face? Does a preschooler learn from eight million scraped web pages sourced from Reddit?

What exactly is a preschooler "trained" on? Thousands of hours of "multimodal data". Assuming that a preschooler sees at 720p, and is awake for 12,000 hours by the age of 3 (about 11 hours a day), they have consumed at least 27 terabytes of video data at streaming-quality compression, or about 3.6 petabytes uncompressed, not to mention audio and sensorimotor data.[^1]

In model-size terms, how large is a preschooler? Trillions of parameters, maybe. [Beren Millidge's estimate](https://www.beren.io/2022-08-06-The-scale-of-the-brain-vs-machine-learning/), which assumes only ~1,000 synapses per neuron, puts the whole brain at an effective 10-30 trillion parameters.

So surely GPT-2 is much more "data efficient" than humans, wielding "preschooler"-level control of language with a measly 1.5 billion parameters and 40 gigabytes of text! And what about GPT-3, which, with only 175 billion parameters and about 1 terabyte of text, [was capable of prose like](https://www.lesswrong.com/posts/vJFdjigzmcXMhNTsx/simulators):

> GPT’s behavioral properties include imitating the general pattern of human dictation found in its universe of training data, e.g., arXiv, fiction, blog posts, Wikipedia, Google queries, internet comments, etc. Among other properties inherited from these historical sources, it is capable of goal-directed behaviors such as planning. For example, given a free-form prompt like, “you are a desperate smuggler tasked with a dangerous task of transporting a giant bucket full of glowing radioactive materials across a quadruple border-controlled area deep in Africa for Al Qaeda,” the AI will fantasize about logistically orchestrating the plot just as one might, working out how to contact Al Qaeda, how to dispense the necessary bribe to the first hop in the crime chain, how to get a visa to enter the country, etc. Considering that no such specific chain of events are mentioned in any of the bazillions of pages of unvarnished text that GPT slurped, the architecture is not merely imitating the universe, but reasoning about possible versions of the universe that does not actually exist, branching to include new characters, places, and events

Only a truly prodigious "elementary schooler" would be able to continue Janus' thought so eloquently. And yet this notion of LLM data inefficiency persists. "Frontier data efficiency lab" Flapping Airplanes, on their front page, [writes](https://flappingairplanes.com/):

> We imagine a world where models can think at the level of humans without ingesting half the internet. The proof that this is possible is all around us: whereas current systems are trained on essentially all of accessible history, humans exceed AI capabilities despite seeing at most a few billion text tokens by adulthood. We estimate that humans are 100,000x-1,000,000x more sample efficient than existing models.

Does this make any sense when you consider that most humans in the history of the species lived never "seeing" a single "text token" by adulthood, or in their entire lives? What do most human "samples" actually consist of? Yet a thesis like this is enough pretense for a $180M seed round and an estimated valuation of $5B.

Even OpenAI's Dan Selsam indulges this notion of data inefficiency, in [an otherwise lucid tweet on AI risk](https://x.com/DKokotajlo/status/2099600298855829616):

> Despite their incredible abilities, the current algorithms seem far inferior to humans in important ways. Most importantly, they still require an extraordinary amount of data to become competent. One could even define intelligence as the efficiency with which one converts experience into competence; by this definition they lag very far behind us.

It's natural that Dan, a capabilities researcher watching the marginal gains from text data go down, would say this. Also, nothing rules out enormous algorithmic advances that squeeze more out of the same quantities of data and compute.

But we really don't understand how humans scale, at all, and so it's absurd to claim that models are "data inefficient" compared to humans. At small scale, the discrete text token-based transformer architecture seems more efficient than anything we've ever seen.[^2]

What about at large scale? As Dan concludes, as far as dangerous capabilities are concerned, it's efficient enough.

*Originally posted on [LessWrong](https://www.lesswrong.com/posts/Fyv5RNMWtESYK2DdL/speak-not-of-data-inefficiency).*
{: .post-crosspost}

[^1]: Yann LeCun does a similar calculation for a 4-year-old's optic nerve and lands at 10^14–10^15 bytes.

[^2]: It's almost as if human language is a "[fully general highly compressed mathematical isomorphism of human cognition](https://x.com/JohnWittle/status/2104668820921069789)". In that case Yann is also wrong, because language is the shortcut to human-level intelligence at current levels of compute; you can just slap robot capabilities and visual intuition on later.
