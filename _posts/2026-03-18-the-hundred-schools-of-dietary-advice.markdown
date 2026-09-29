---
layout: post
title:  "The Hundred Schools of Dietary Advice"
date:   2026-03-18 16:39:20 -0400
categories: writing
excerpt: "Why is there so much conflicting dietary advice? Two classical Chinese philosophers offer two heuristics for making sense of pluralism."
math: true
---

Why is there so much conflicting dietary advice nowadays? For a moment, take the perspective of a layperson who doesn't know how to identify a sketchy observational study in the field of nutrition. Your only intel is [Diary of a CEO](https://en.wikipedia.org/wiki/The_Diary_of_a_CEO) videos and maybe what shows up on Google when you search things like "are eggs healthy".

You watch a video where one MD with a [positive-sounding Wikipedia page](https://en.wikipedia.org/wiki/Will_Bulsiewicz) ("American triple board-certified") explains it all in terms of fiber and the microbiome. But another [two](https://www.diagnosisdiet.com/) [MDs](https://bozmd.com/) and a [PhD](https://benbikman.com/) claim that it's all about ketones. There is *some* common ground—more fresh whole foods, less frozen pizzas and the like—but who knows when it comes to cholesterol or whether ketones cure cancer. Without anything better than this fire hose of contradictory information, you might come to conclude some mix of the following two views:[^1]

1. There is no one diet perfect for everyone.
2. Experts are incentivized to make exorbitant claims which get them attention on the internet. This translates into book sales, supplement sales, clients for their clinic, etc.

Considering this suboptimal epistemological environment, I'd say these conclusions aren't half bad. Also, these reactions generalize beyond just nutrition; I'd conjecture that they're two of the main heuristics that people fall back on when faced with pluralism.

By "pluralism," I refer to the proliferation and persistence of multiple distinct (mostly mutually exclusive) views in a field, with at least two views being substantially popular.[^2] Some level of disagreement is common across all frontiers of human knowledge, but in pluralistic domains, the formation of opposing schools is the status quo. Many of these domains are widely considered unscientific while also enjoying privilege as important fields of human inquiry.[^3]

A rationalist tries to look at the evidence and form judgments independently. But it's nice to use as much information as possible, and the state of the field is information. Can we use it?

The two heuristics above hint at two distinct approaches. The first is to respond by updating one's belief of whether the underlying question (in this example, what the optimal diet is) has an answer at all. The second treats the presence of pluralism as mostly independent from the answer to the underlying question.

These two heuristics also correspond to Zhuangzi and Han Feizi, two philosophers from the Hundred Schools of Thought period in classical China. Intellectual pluralism has emerged in many times and places in human history, but the Hundred Schools period had a special quality: every philosopher was trying to explain, devalue, and maybe even eliminate this pluralism, little more to them than a confusing and unproductive mass of contradictory beliefs.

## Zhuangzi

Zhuangzi was a thinker who lived during the mid-Warring States period.[^4] By his time, the Hundred Schools of Thought period was well underway; "traveling scholar/thinker" was now an established profession. In contrast to the Greeks, who sometimes indulged in frivolous subjects like metaphysics and natural philosophy, the Chinese classical thinkers kept the debate largely to ethics and political theory.

There were two dominant factions of scholars. The first sought to emulate Confucius, who outlined a kind of [religion without spirituality](https://en.wikipedia.org/wiki/Waking_Up:_A_Guide_to_Spirituality_Without_Religion).[^5] The second rallied around Mozi, who argued for a level of ethical impartiality approaching that of Peter Singer (though unlike Singer, he planned to implement it through a hierarchical authoritarian state based on the just world hypothesis). In the centuries since their beginnings, each group subdivided into dozens of schools who filled in the ambiguities in their founders' words in slightly different ways. There were also many fringe thinkers, including the "School of Names," which produced paradoxes of space (e.g. "That which has no thickness cannot be accumulated, and yet it can be a thousand leagues large"), akin to Zeno of Elea, and paradoxes of language (e.g. "a white horse is not a horse"), faintly resembling Antisthenes' struggle with particulars.

In the face of this flourishing intellectual diversity, where schools that had promised an end to the chaos of ethical heterodoxy (Mozi's) were fragmenting at comical rates and logicians grew famous for defending statements that were intuitively contradictory, Zhuangzi concluded that human inquiry was a function that wasn't converging. Nobody could find convincing answers because the type of answers they were looking for, ones that were universal and definitive but also fit nicely and consistently into human language and comprehension, simply could not exist.

(You may find the first lines of the below annoying. Reading them slowly helps.)

> "Nie Que asked Wang Ni, 'Do you know what all things agree upon as right?'
> 
> Wang Ni said, 'How could I know that?'
> 
> 'Do you know that you don't know it?'
> 
> 'How could I know that?'
> 
> 'Doesn't anyone know anything?!'
> 
> 'How could I know that? But even so, suppose I tried saying something. How could I possibly know that when I say I know something, I don't not know it? How could I possibly know that when I say I don't know something, I don't know it?
> 
> Let me try asking you something. If people sleep in the damp, their backs hurt and they wake half-paralyzed. But is this true of an eel? If they live in trees they shudder with fear. But is this true of a monkey? Of these three, then, which knows the right place to live?
> 
> ...
> 
> People say that Maoqiang and Lady Li are beautiful. But if fish saw them, they would dive deep; if birds saw them, they would fly high; if deer saw them, they would cut and run. Of these four, which knows beauty rightly? From where I see it, the sprouts of benevolence and righteousness[^6] and the pathways of right and wrong are all snarled and jumbled. How would I know the difference between them?'"
> 
> *Zhuangzi* 2.11

### Suppose the answer doesn't exist

Let's try to formalize Zhuangzi's response a little. Suppose that there is a non-zero probability that our question of interest doesn't have an answer. Call this Event A. Maybe our question is analogous to asking "what is the best diet for an animal?", as if this had nothing to do with the species.

Now we observe that pluralism exists with regard to the answer of that question. Call this Event B.

Now, surely $$P(B \mid A) \ge P(B)$$. If there is an answer, people at least have a shot of eventually finding it and making the disagreement go away. If the question doesn't have an answer, anyone who debates it will be doomed to endless confusion. Intuitively, conditioning on the nonexistence of the answer increases the chance of pluralism arising.

So using Bayesian updating, $$P(A \mid B) \ge P(A)$$. We can conclude from our confused experts that the question is less likely to have a definitive answer.

Now, there are a lot of problems with this formulation. For example, how can we possibly get a reasonable prior? How can we estimate what proportion of human questions are answerable? If we limit our consideration to high-profile cases (e.g. what is the meaning of life), it's hard to say whether $$A$$ has ever occurred: if $$A^{C}$$ (i.e. we observe that the question *does* have an answer) hasn't occurred yet, then usually at least some people are still debating the question.

We can, however, find several fields—like chemistry, astronomy, medicine, and taxonomy—where lots of ancient questions resolved to $$A^{C}$$. Plato's *Apologia* depicts a disagreement in ancient Athens on whether the moon was a physical object (i.e. a distant rock) or a supernatural object (i.e. a god). What would it even mean in this case for $$A$$ to be true? That is, if there was no answer for what the moon was?

If we want to avoid some of the weirdness of this approach, we can turn to a philosopher who was a bit more pessimistic about human motivations.

## Han Feizi

Han Feizi was a thinker from the late Warring States period. He was likely a student of Xunzi, a leading Confucian thinker of the era who was widely versed in previous thinkers, including Zhuangzi.[^7] But Han Feizi's real intellectual idol was a thinker named Shen Dao.[^8] Shen Dao argued that the success of a state depended not on individuals choosing to behave benevolently or righteously, but on the correct channeling of individual self-interest.

As a result, Han Feizi's explanation for the proliferation of scholars and thinkers was not about the insufficiency of language or the subjective nature of virtue. It was that rulers were paying their subjects to be lazy:

> "Now, if people can, by cultivating the cultural arts and practicing eloquent speeches, obtain the fruits of wealth without the dangers of war, who would not do so? Thus, for every hundred who pursue wisdom, there will only be one who employs his physical strength to farm or fight."
> 
> *Han Feizi*, Chapter 49, "The Five Vermin"
> 
> "Heavily taxing farmers while substantially rewarding scholars and yet hoping to exhort the people to work hard while spending little time in discourse, this cannot be accomplished."
> 
> *Han Feizi*, Chapter 50, "The Illustrious Schools of Thought"

Han Feizi's diagnosis of pluralism was not an intellectual exercise. Pluralism was an issue:

> "If those who pursue wisdom are numerous, the law will be defeated. If those who employ their physical strength are few, the state will become poor. This is why the age is in disorder."
> 
> Chapter 49

If a state solved this issue, its rulers would stop being confused by the various contradictory schools. They could establish a functional bureaucracy, agricultural economy, and military; conquer the other states; and bring peace to the world—a clear net benefit for everyone. So Han Feizi proposed a solution:

1. Introduce harsh regulations on trade and travel to incentivize people to become farmers and soldiers and disincentivize them from becoming traveling scholars and thinkers.
2. Bury all of the current scholars and thinkers alive.[^9]

These were implemented and led to the unification of China under the Qin state.

### Who cares if the answer exists?

A Han Feizian response to pluralism usually involves waving away the underlying question. If it's possible for so many people to disagree for so long and never come to a solution, the question must not be tractable or worth caring about. It's more informative to try to diagnose the pluralism in terms of human motivations and incentive structures.

This is different from declaring the question unanswerable. See how Han Feizi describes the disagreement between the Confucians and Mohists:

> "Thus, after the deaths of Kongzi \[Confucius\] and Mozi, the Confucians divided into eight groups while the Mohists separated into three. The doctrines that each accepts and rejects are mutually contradictory and not the same, and yet each group claims that they are the true representatives of Kongzi or Mozi. Kongzi and Mozi cannot be brought back from the dead, so who should decide which of the schools of our age is correct?"
> 
> Chapter 50

A question like "would Mozi prefer Mohist school #1 or Mohist school #3?" could certainly be answerable. If some new fragment of Mozi's writing was discovered, it might provide the necessary evidence. The problem is not about the existence of an answer; it's merely that the extant evidence is not sufficient.

We can formulate Han Feizi's approach like this: even if $$P(A) > 0$$, $$P(B \mid A^{C})$$ is usually sufficiently close to $$P(B \mid A)$$ that the Bayesian update is negligible. That is, there is a chance of pluralistic confusion arising even if a definitive answer exists (e.g. the Athens moon disagreement), and it might last for an indeterminate length of time. There is also a chance that pluralistic confusion doesn't arise even if a question doesn't have an answer; maybe orthodoxy is enforced, or people just stop caring about the question.

So a lack of available evidence can make $$A$$ basically irrelevant. We can reasonably attribute the failure of the Greek philosophers to definitively answer their questions about medicine, physics, etc. to this lack of evidence. Fields that study the behavior of humans and groups of humans suffer from this as well, since the confounding variables are so numerous and the units we would like to explain (e.g. countries, societies) are too large and complex to run randomized control trials on.

But why would experts continue to disagree energetically if no productive inquiry was realistic?

### Motivated reasoning

Nutrition science is a field where a lot of consumer money is at stake. All of the doctors I mentioned are selling something on their sites. They're analogous to the traveling scholars of Han Feizi's time, except that they provide advice on how to lose weight rather than conquer China. More insidiously, corporations are incentivized to fund research positioning their products as healthy.

But I suspect that a better explanation goes beyond mere profiteering. The extreme difficulty of avoiding motivated reasoning, not just for experts but for everyone involved, is a *feature* of fields that display pluralism. Individual profit-seeking experts tend to follow the curvature of this motivation field rather than create it.[^10]

Consider dietary advice. People want to eat certain things and are saddened if they are told those things are unhealthy. At the same time, they might feel like they should and shouldn't eat certain things, maybe because of ethics (e.g. veganism), or maybe internalized conditioning (e.g. margarine is healthier than butter). It might also be a matter of signaling; a carnivore diet indicates right-skew and masculinity, a vegan diet indicates left-skew and empathy. The discipline of an extreme diet also has its own rugged appeal. All of this could create resistance in the face of contradictory evidence.

And that barely even scratches the surface. Eating is one of the activities we do the most frequently and regularly, and yet, unlike sleeping, breathing, and walking, it varies massively between individuals and cultures. It's a defining feature of our interpersonal and personal lives. It has to do with identity and deep psychological factors that would rather not be coldly scrutinized by the uncomprehending glare of Reason.

Now consider mathematics. Very few people identify strongly with algebraic structures or concepts in differential geometry. Inducing people to be deeply invested in math is usually treated as a sign of pedagogical genius rather than a crime against rationality. Taxonomy, a field roughly in between, shows intermediate levels of distortion: significant friction around human evolution but the gradual adoption of a consensus.

To put this in an extremely tenuous statistical framing, you would expect some form of the Central Limit Theorem to apply in most fields. As the number of well-intentioned experts increases, the sample average of their views on any given question should converge, if slowly, towards the truth. But in pluralist cases, the motivated reasoning adds in correlation between the experts. Add in a little variance across individuals from genetic factors and upbringing, and it will stick around as $$n \to \infty$$.

## Conclusion

The ideal that each individual should weigh the evidence for themselves and come to their own conclusion through individual inquiry is a great principle. But in the absence of time or resources, people sometimes fall back on two heuristics that utilize the observation of pluralism within a topic, one Zhuangzian in character and the other Han Feizian. Fortunately, these heuristics provide reasonable defaults, especially when the amount of experts is large.

They can certainly fail, since the range of experts visible to a person could be extended or truncated. A truncated range (e.g. living within a bubble where only one view is presented) would produce false indicators of a decisive answer for both heuristics. An extended range (e.g. a corporation funding experts to support a position with weak evidence) could cause a Zhuangzian to incorrectly fall into relativism. Conversely, a Han Feizian might think conspiratorially and suspect an artificially extended range of experts when the real cause is underlying ambiguity. This is an issue with heuristics: an identical observation can suggest two opposing impulses, and there's no rational way to choose between them.

Despite this, the instinctive action of these heuristics preserves what I view as a deep and sacred human impulse, one that calls alluringly towards transcendence. What if the question everyone else is asking is on unstable ground? Isn't it worthwhile to note the persistent disagreement of everyone else and question the question itself, rather than just joining in the cacophony? Kant tried to do this with metaphysics in his *Critique of Pure Reason*. Jung continued this effort and extended it to religion in his *Psychological Types*. I personally find their efforts compelling, but as to whether they were on to something, the jury is still out.

(All citations from philosophers are from *Readings in Classical Chinese Philosophy,* Third Edition, edited by Ivanhoe and Van Norden. Their interpretation and choice of translations likely had a strong influence on my presentation of these thinkers.)

*Originally posted on [LessWrong](https://www.lesswrong.com/posts/MB46FsKPyiDTbzRZu/the-hundred-schools-of-dietary-advice).*
{: .post-crosspost}

[^1]: This whole scenario and the resulting responses are based my parents' experience.

[^2]: This may not be a standard usage of "pluralism". The closest definition I could find is from Cambridge Dictionary: "the existence of different types of people, who have different beliefs and opinions, within the same society".

    I would like to know if this is an abuse of the term.

[^3]: In addition to dietary science, these fields seem like they currently display a substantial level of pluralism:

    - Ethics
    - Quantum physics (?) (i.e. string theory vs. quantum gravity)
    - Political philosophy
    - History (especially in the interpretation of causality)
    - Sociology (?)
    - Psychology (?)
    - Religion
    - Metaphysics

    I know very little about the fields marked with (?).

[^4]: Zhuangzi, or most of the things attributed to him, could be mythical. If so, this paragraph merely describes the character depicted in the work called the *Zhuangzi.*

[^5]: As in, a maximally [orthopraxic](https://en.wikipedia.org/wiki/Orthopraxy) religion. Puett, Ivanhoe, and Van Norden argue that Confucians valued ritual for how it structured human relations and that Confucius himself gave little credence to any supernatural aspects. For further discussion see [this paper](https://puett.scholars.harvard.edu/publications/%E2%80%9Ccritical-approaches-religion-china%E2%80%9D) by Puett.

[^6]: Benevolence (rén, 仁) and righteousness (yì, 義) are two key terms in classical Chinese ethics. Their meaning varies slightly from thinker to thinker. Mencius defines benevolence as compassion and caring, especially towards family, whereas righteousness is more about propriety, especially in one's conduct towards authority.

[^7]: Xunzi has his own reaction to pluralism. In the dietary example, it would be something like:

    "Most of the experts know some important aspect of what makes a good diet, but many of them take it too far. The optimal diet is a balance of the extremes."

    This is a nice heuristic that works for a lot of people in practical cases. It also provides justification for protecting pluralism.

    However, I don't find Xunzi's explanation for why pluralism persists in spite of the existence of a single answer particularly compelling. It can be interpreted as a version of Han Feizi's (the other thinkers fixate on overly specific subjects out of pride and the desire for fame). Or it could be interpreted as "the other thinkers are too virtueless and unwise, unlike Confucius, who was so virtuous and wise that he didn't get stuck on one thing. Nobody else has been as good as Confucius since then," which doesn't offer much in terms of rationality. (This is based on *Xunzi* Chapter 21, "Undoing Fixation".)

[^8]: Shen Dao is also potentially mythical.

[^9]: Han Feizi didn't suggest live burial directly, but it's the spirit that counts.

[^10]: Less so for corporations, which I think is what makes them more dangerous.
