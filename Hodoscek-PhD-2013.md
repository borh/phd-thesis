% Contextually Aware Writing Assistance System for Japanese
% Bor Hodošček
% 2013/4/4

\part{Background}

# Introduction

First, I would like to present the outline of my thesis, which consists of four chapters.
As my research touches on several different academic fields such as linguistics, natural language processing and educational technology, the introduction and literature review in Chapter 1 will provide the necessary background for the succeeding chapters.

Chapter 2 will introduce the model of context, which consists of three models: the register model, then the topic model, and finally the readability model.

In the next chapter, Chapter 3, entitled writing assistance system, I will introduce two writing assistance systems developed in collaboration with other researchers as marked in the slide.
The first writing assistance system is called Natsume, while the second, made to cover some shortcomings in the first, is called Nutmeg.
Finally, a system that encapsulates the models listed in chapter 2 will be proposed.

**Something about why/how the new system is significant**

Chapter 4 will conclude my thesis.

## Writing and Communication

![Adapted from @schramm1955's communication model](images/schramm-model.pdf)

A _common field of experience_ is essential to communication.

To begin with, how do we define how people communicate?
In Wilbur Schramm's model of communication, the source and destination can be thought of as being the two people as seen in Figure 1.
We see the source is encoding some concepts she wants to communicate, which are then turned into the signal in the center of the screen.
This signal is then decoded by the destination.

But what is then controlling the decoding and encoding?
It is the notion of a field of experience and is central to the model described here.
The field of experience can be defined as the beliefs, values, experiences and learned meanings of an individual.
It is when there is an overlapping of these fields between two people that the signal can be successfully encoded and decoded.

As we will see later, the type of communication I will be talking about from now on is written communication.
Specifically, one in which a writer is trying to communicate to a reader that he might not be able to get feedback from.
It is thus one-way communication.
Also, what follows from this is that in order to be understood, the writer must accommodate the reader --- he must close the field of experience gap between him or her and the reader in the only way possible --- to /increase his own field of experience/.


-   The writer can only convey as much information as the reader can decode \rightarrow knowledge of target audience is essential

-   can humans correct learners papers?
    -   i.e., can they give reasons for learner errors WRT genre/register
    -   can we describe the genre schema of experts?

-   does telling writers their text is not fit for their target genre useful?
    -   it raises their sensitivity
-   best writing assistance: writing centers in the US?? staff talks through the essay with the writer, in a tight feedback loop (check [@Bawarshi2010])

-   what is the minimum language proficiency required to make use of writing assistance systems?

## Computer-Aided Writing Assistance

-   Online dictionaries
-   Spell checkers
    -   No equivalent for Japanese, because of prevalence of smart Input Method's such as Google IME
-   Grammar checkers (for Japanese)
    -   Effective in specific domains in English [@hoard1992automated], or specific sub-set of grammar such as case-particle misuse [@Mizumoto2012E]
-   Style checkers (for Japanese)
    -   Prescriptive style manuals; Yahoo! Japan's [_Kousei shien_](http://developer.yahoo.co.jp/webapi/jlp/kousei/v1/kousei.html) service

-   Increasing trend to leverage large-scale language data for automated writing assistance

Before revealing my research aim, I would like to briefly summarize the field of computer-aided writing assistance, especially as it pertains to Japanese.
Online dictionaries and especially Japanese language input environment play a large role in many writers lives, but these provide little help in automatically checking for problems in meaning or grammar.
Grammar checkers have predominantly been limited in scope, a good example is a recent system that only looks for Japanese particle misuse.
Style checkers mostly help to identify common style incongruities like the distinction between desu-masu and da-dearu forms.

All in all, there is an increasing trend to take advantage of large-scale language data for these tasks.

Problems with the Word+dictionary (browser) writing method:

-   mostly stops at the word level
-   some level of grammatical checking, but rule-based
-   provides no scaffolding (active checking and suggestions based on the learners current text) or integrated writing

At what level can writing be automatically improved?

-   Spelling checkers
    -    Less applicable to Japanese because of the presence of intelligent Input Method Environments (IME)
-   Grammar vs. style checkers (cf. [@heidorn2000intelligent])
    -    Domain-specific grammar checkers can be effective (cf. Boeing's [@hoard1992automated]), but require considerable manual tuning and rule creation
-   Direct or indirect feedback?
    -    Indirect feedback preferred because it forces the writer to reflect [@godwin2008emerging]

-   what are the main evolutions (revolutions) in writing on a computer compared to, say, a typewriter or pen?
-   similar systems (feature matrix?)
    -   Newer efforts: Coori, lang-8
-   domain-specific grammar checkers have been found to be effective (cf. Boeing's [@hoard1992automated]) provided they encode domain-specific rules into the engine, which is time-labor intensive

> What tends to be of most use to learners is indirect feedback, which points to problems in written
> work but leaves it to the writer to find the solution. This requires the learner to reflect on the
> application of language rules to one's own actual writing. Many language teachers use codes (such
> as John Lalande's ECCO - error correction code) to mark student writing. -- [@godwin2008emerging]

: Feature matrix

Feature                  System 1  System 2
----------------------- --------- ---------
Spelling correction(*)
Thesaurus
Collocation checking
----------------------- --------- ---------

*: Spelling correction makes less sense in Japanese than for some other languages; the IME prevents many errors.

-   put all systems along writing assistance vs. general L2 learning systems axes?

## Research Aim

Construction and evaluation of writing assistance system for Japanese based on the concept of writing context.

Construction:

-   Models of context **(Ch. 2)**
-   Web-based writing assistance system **(Ch. 3)**

Evaluation:

-   Evaluate models of context **(Ch. 2)**
-   Evaluate system features  **(Ch. 3)**

Finally, the aim of my research is to construct and evaluate a writing assistance system for Japanese based on the concept of writing context.

With respect to construction, I am referring to both the construction of the model of context in Chapter 2, as well as the construction of a web-based writing assistance system in Chapter 3.

With respect to evaluation, I am referring to the evaluation in of the models of context in Chapter 2, as well as the evaluation of the system in Chapter 3.

# Contextual Model

## Introduction

## Writing Context Revisited

!!! FIX と→て
＋共同研究

![](images/schramm-context.pdf)

Explain context in terms of writing intent, register, genre, topic, readability, etc.

-   Sketch out the area my research aims to address, i.e. the micro vs. macro levels of writing assistance
    -   What does it mean to focus on the micro?
    -   Why not do the macro, what are the limiting factors in our understanding/technology that prevent us from doing so?

Should show how different people have different register and topic knowledge and how this  is transferred to and from the text.

![Adapted from @schramm1997communication's communication model (p. 54) with additions by me in blue](images/schramm-model-new.pdf)

-   the field of experience = writing and reading context = topic/domain knowledge, register (style) knowledge, readability, ...


Here we describe our model of context in terms of three concrete models: **register**, **topic** and **readability**.
These models are not independent of one another, but are discussed separately for reasons of clarity.

-   Outcome: 3 models (or 3 sets of models) which, when combined, account for the **register**, **topic** and **readability** of a text

-   especially when dealing with register and topic, the interrelation is complex and, depending on NLP constraints, the line can become blurred (to the point of the distinction not making sense anymore?)


Bridging the context between writer and reader:

-   differences in register, topic knowledge and readability (general vocabulary knowledge, grammar knowledge)!!

Register, Topic and Readability:

Topic and register are two extremes on a cline.

![Relations between register, topic and readability](images/register-topic-readability.pdf)

For every model, we want to be able to:

-   Measure differences in model fit according to corpus
-   Compare writing input model fit to the other corpora

Should show how different parts of the text and sentence manifest themselves as register and topic.

**The problem with words and, by extension, collocations, is that they are not purely topical or purely functional --- need both to assess correctly.**

## Context and Corpora

-   Data-driven approach to writing assistance where **context is modelled on differences in corpora**
-   Multiple corpora varying in register, topic and readability


1.  Scientific and Technical Japanese Corpus (STJC)
2.  Balanced Corpus of Contemporary Written Japanese (BCCWJ) --- contains 10 sub-corpora
3.  Japanese Wikipedia

\begin{table}
\small
\centering
\caption{\footnotesize Different corpora employed in this research (STJC = ; BCCWJ = )}
\vspace{.3em}
\begin{tabular}[c]{ll|r}
\toprule
\multicolumn{2}{c|}{\textbf{Corpus}} & \textbf{Characters}\\
\midrule
& \textbf{STJC} & 6,108,143\\
& \textbf{Wikipedia} & 372,901,202\\
\midrule
\multirow{8}{*}{\textbf{BCCWJ}} & Books & 53,801,124\\
& Yahoo! Q\&A & 9,763,298\\
& Diet minutes & 8,712,108\\
& Textbooks & 1,818,571\\
& White papers & 8,443,965\\
& Yahoo! Blogs & 5,246,121\\
& Magazines & 455,634\\
& Newspapers & 1,188,355\\
\midrule
& Total & 468,438,521\\
\bottomrule
\end{tabular}
\end{table}

## Register Model

**Register definition:** _variation in language directly connected with the situation, or context, of its use._

Examples

-   Spoken vs. written language
-   Formal, academic prose vs. informal, casual prose

-   Proposed models

    N-gram language model, function word model, tf-idf ($\rightarrow 0$) vector space model

**Outcome**: Infer the register of text.

Manifestation in language:

-   Register can be quantified by comparing corpora (databases containing collections of text) belonging to different genres [@ALAHodoscek2011]


### Register Identification Method

\fullcite{ICJLEHodoscek2011E}

1.  Perform the $\chi^2$ test for variance on the relative frequency $f$ of a word or collocation on all corpora $C_0, C_1, \cdots, C_K$

    $$\Delta f(k) =
    \begin{cases}
    f(k) - \bar{f_K}, &\text{if } \frac{(f(k) - \bar{f_K})^2}{\bar{f_K}} > \chi^2(\text{df}=K-1; p=0.05)\\
                   0, &\text{otherwise}
    \end{cases}
    ; k \in K$$
2.  Assign corpora to the positive ($C_+$) and negative ($C_-$) groups, compare their sum, and compute the score $s_i$

    $$s_i=
    \begin{cases}
     1, & \text{if } (\sum_{j \in C_+}\Delta f_i(j) \ge 0) \wedge (\sum_{j \in C_-}\Delta f_i(j) < 0) \rightarrow \text{correct usage}\\
    -1, & \text{if } (\sum_{j \in C_+}\Delta f_i(j) \le 0) \wedge (\sum_{j \in C_-}\Delta f_i(j) > 0) \rightarrow \text{incorrect usage}\\
     0, & \text{if neither is statistically significant} \rightarrow \text{no result}
    \end{cases}$$

Proposed Model:

-   Compare existing models and choose the best one (tf-idf based, word class based, \ldots)

-   \parencite{ALAHodoscek2011} (refereed)

    How to tie this in with my final model: emphasize the theory behind the method, it was a stepping stone to other models

-   Master's thesis

    The arbitrary separation of functional and content words was useful, but neglected to take into account differences in topic distributions between genres

Create per model:

Table: Models

+----+----+----+----+
| G1 | G2 | G3 | ...|
+----+----+----+----+
| G1 |  1 | 0.6| ...|
+----+----+----+----+
| ...| ...| ...| ...|
+----+----+----+----+

-   distances are? from MD analysis?????! Or just model comparisons?
    -   (Yamagen) use mid-level tf-idf words (can be a small amount, must be relatively common, should be common in all genres), compare freq. matrices
    -   cells should include cf-idf scores for (word1, word2)
    -   Which language level is more appropriate? lemma, kihon-kei, or surface?

-   n-gram language model
    -   by making a language model per genre, it is possible to fit any text to a genre
    -   comparing models may reveal quantifiable differences in the genres
    -   to get distance between n-gram models, use model from genre 1 to score texts from genre 2
    -   disadvantage: does not differentiate between content and function words

## Topic Model

**Topic definition:** _the subject of a text. Does not necessarily refer to the subject of a sentence. One or more topics per text._

-   Proposed models [@NCHodoscek2012E]

    Probabilistic topic model (Latent Dirichlet Allocation), tf-idf ($\rightarrow max$) vector space model

**Outcome:** Infer the topics of a text.

-   same as previous (LDA), or maybe DMR (Dirichlet-Multinomial Regression: using genre labels as features)
    -    one model per corpus or one big model?

-   Investigated relation between sub-corpora of the BCCWJ $\rightarrow$ topic $\ne$ register
-   Proposed Models


-   find topics which tend to appear in only one genre -- i.e. check the genre distribution of topics
-   check collocation/word's topic distribution and compare it to the register distribution

### Latent Dirichlet Allocation Topic Model

![Latent Dirichlet Allocation topic model used in [@NCHodoscek2012E] (unrefereed)](images/lda-topic-model.pdf)

Proposed Model:

-   same as previous (LDA), or maybe DMR (Dirichlet-Multinomial Regression: using genre labels as features)
    -    one model per corpus or one big model?

-   find topics which tend to appear in only one genre -- i.e. check the genre distribution of topics
-   check collocation/word's topic distribution and compare it to the register distribution


## Readability Model

**Readability definition:** _quality of text that makes it easy or hard to understand._

-   Proposed models [@CASTELJHodoscek2012]

    A combination of vocabulary, collocation, syntactic structure and language-model based readability measures

**Outcome:** Grade readability of text, sentences, collocations and words.

Readability is the result of interaction between the text (content, style, design, ...) and the reader (prior knowledge, reading proficiency, motivation, ...).

Readability as aspect of context.

Readability at the micro and macro scales:

-   micro: sentence readability
-   macro: logical structure readability

-   Why do we focus on the micro?
-   What are the problems with extending the micro readability measures to the macro scale?

    (Even if the text uses easy to understand words, the meaning cohesion might be bad and confusing to read. The point is that when giving feedback to learners on the readability of their texts, we should be wary of using micro-measures. The obi-2 measures work out because they expect professional writing (what about Yahoo! & friends?).)

In @schramm1997communication's model:

-   reader decoding capacity > writer encoding capacity \rightarrow writer can/should use higher-level words, expression and grammar that are common in the chosen domain
-   reader decoding capacity < writer encoding capacity \rightarrow writer can/should add redundant information, use lower level words, expressions and grammar

-   Output (not write overly-convoluted sentences, be able to write for the readers level)
-   Input (searching for expressions/examples one is more likely to be able to understand)

-   do more errors in learner corpora translate into harder to read texts (WRT readability measures; what parameters are most responsible for this)?
-   readability measures are not reliable on short text (or one sentence in general), so often the most simple measures, like sentence length, are powerful enough
    -   use whole-text readability only

Previous Research:

1.  Vocabulary-based (JLPT)
2.  Collocation-based
3.  Syntactic structure-based
4.  Language model-based (Obi2)

Proposed Model:

-   [@CASTELJHodoscek2012]
-   JLPT word list
-   BCCWJ word list (Matsushita TM list (Tokyo Univ.): [日本語を勉強する人のための語彙データベース](https://www.google.co.jp/url?sa=t&rct=j&q=&esrc=s&source=web&cd=1&cad=rja&ved=0CC4QFjAA&url=http%3A%2F%2Fwww.wa.commufa.jp%2F~tatsum%2FVDLJ_Ver1_0_International-Students.xlsx&ei=owAaUfOXDO_vmAXvmoHwDA&usg=AFQjCNHMEPokeGPt7vQlSf-J78ZxHcXhsg), Tsukuba Univ. list: [日本語教育語彙表](http://kotoba.nuee.nagoya-u.ac.jp/jc2/base/))
-   Obi2

\part{Writing Assistance System}

# Introduction

## System Architecture Overview

![System architecture](images/system-architecture-overview-3.pdf)

Composable system architecture (vs. contextual --- plugin-based).

# [Natsume](http://hinoki.ryu.titech.ac.jp/natsume/)

![Natsume overview](images/natsume-overview.pdf)

## Collocation Search Interface

![Natsume collocation search interface](images/natsume-compare.pdf)

## Genre Comparison Interface

![Comparing collocations of 'jikken' with 'yaru', 'suru' and 'okonau' across genres](images/natsume-genre-compare.pdf)

-   writers use the genre comparison feature of Natsume to decide if their word choice is correct for their chosen register
-   problem identified in Natsume evaluation: how to make writers aware of problems in their writing that they do not actively search for?

## [Natsume](http://hinoki.ryu.titech.ac.jp/natsume/) Evaluation

Compare: Natsume+word processor vs. word+dictionary

### Evaluation 1:

-   **Informal$\rightarrow$formal sentence rewriting task** with 40 undergraduate participants (January 2011)

    Negative linear relationship between language proficiency and improvement in task

### Evaluation 2:

-   **Report writing task** with 20 undergraduate participants (June 2011)

    Participants did not search for words they believed were correct

-   User profile: Intermediate-Advanced learners of Japanese, Japanese native speakers
-   Enables learners to search for words and word patterns
-   Helps them to make correct use of these patterns according to their writing goal (i.e. paper)
-   Follows the philosophy of data-driven language learning (authentic examples, exploration, etc.)

# [Nutmeg](http://hinoki.ryu.titech.ac.jp/nutmeg/)

Writing assistance system that identifies errors in **reports and academic prose** [@NCYagi2012E].

-   Reduce cognitive burden associated with switching between applications while writing
-   Detect errors that learners themselves are unaware of

![Numteg interface summary](images/nutmeg-interface-summary.pdf)

## [Nutmeg](http://hinoki.ryu.titech.ac.jp/nutmeg/) Error Feedback

-   Underlines errors and provides feedback on mouse hover
-   When possible, provides an explanation of why the system thinks there is an error

![Nutmeg writing interface](images/nutmeg-writing-interface.pdf)

# Final system

## Correction Based on the Contextual Model

### Proposed Method (1): Employed in Nutmeg

-   Formalization of manual comparison method in Natsume
-   Limited to correcting paper and report writing, by comparing formal/academic corpora with informal/spoken corpora
    -    STJC + White papers $\rightarrow$ proxy corpora for paper and report writing
    -    Diet minutes + Yahoo! Chiebukuro + Yahoo! Blogs $\rightarrow$ proxy for informal/spoken writing

## Correction Based on the Contextual Model

### Proposed Method (2): Based on Model of Context

Use the three models of context (register, topic and readability) to provide corrections based on writing context.

-   distances between corpora used to weight the occurrence of some word or collocation depending on the writing context

Problems with the previous model:

-   the choice of positive and negative corpora are "ad-hoc", based on researchers perceived differences between corpora

Proposed method:

-   use the three models to measure the distances between corpora
    1.   register model (TODO)
    2.   topic model
    3.   readability model

## Final System

Online browser-based editor with integrated feedback features containing the three models of context.

Two levels of assistance:

1.  Word and collocation level
    -   Register: identify register misuse in words and collocations
    -   Topic: identify words and collocations with similar topics
    -   Readability: identify word level

2.  Text level
    -   Register: identify closest registers to input text
    -   Topic: identify topics similar to input text
    -   Readability: identify sentences with low readability, provide readability report for whole text

Features:

-   all aspects of the system act on the knowledge of the writer's proficiency level, chosen writing topic and target audience
-   identify and provide corrections for word and collocation usage that are specific to the writer's target *register*, *topic* and *readability* (direct feedback)
-   show the writer how close the writing is to multiple genres, with respect to register, topic and readability (indirect feedback)

-   what features should we allow the user to set: i.e. language proficiency, genre knowledge, reader language prof+genre knowledge

## Evaluation

### Evaluation (1): Data

-   Classification performance of models
-   ['Natane'](http://hinoki.ryu.titech.ac.jp/natane/) Japanese learners corpus: contains around 200 corrected reports and essays by Japanese learners
    -   Measure the precision and recall of correction features

Natane (cf. [@dale2012framework], ["Helping Our Own" project](http://clt.mq.edu.au/research/projects/hoo/)).
-   One "problem" with Natane is the inclusion of a lot of register annotations/corrections that might not appear in other more general essay-like learner corpora, but as this is the point of my research, this is a given and should be said up-front

### Evaluation (2): Experiment

-   Japanese learners and native Japanese speakers

Two kinds of experiments:

-   Focus on making writers more aware of the differences in topic and register
-   Focus on the measuring the improvements in writing due to the system
    -   By measuring diffs of the writer's writing (can get rid of differences in writers' proficiency level)
        (i.e. differences in Malatti and Chinese writers in Natane)
    -   If we have people give use their writing (in-progress), we can see how they correct it with the system
    -   What writing task?
        -   What topic to focus on?
        -   Is it the right register?
        -   Change writing task depending on learner's backgrounds?
    -   When comparing

Experiment setup must be completed in March.

More comprehensive experiment, focused on evaluating the three contextual models; might end up too complicated --- how to measure everything?

-   check if experts agree with our system/models
-   the application of the models differs depending on what is being classified: word, collocation, sentence or whole-text

E-mail writing correction: could be possible if we split the Yahoo!Q&A documents into two parts: question and answer.

Use spot/[J-CAT](http://www.j-cat.org/en/) to measure participant language proficiency

\part{Conclusion}

# Conclusion

Proposed novel method for using writing context for writing assistance.

1.  Depends only on genre-labeled language data
    -   Writing contexts other than report writing can be added as long as there is sufficient language data
2.  Possible to increase learner awareness towards differences in language
    -   Close the experience gap between second language and native writers, non-experts and experts

-   compared to existing systems that do not take into account the writer's context, \ldots


作文支援システム構築のため、言語資源を用いて、自然言語処理で可能な部分を実現させること

教育（学習）的視点からは、レジスターの理論的フレームを利用して、学習者（論文などを書く必要のある留学生）に　レジスターの概念を意識化させることをある程度実現したということだと思います。

理論的には、　教育工学ではdata　driven　learning　、言語学では機能文法（Halliday）,Topic理論、言語処理では、統計手法（Biber を含む）機械学習の考え方... このような理論的な枠組みで新しい考えがどう埋めれたかをアピールすることが最も重要です。

つまり、今までなかったもの、できなかったことをどのようにして、新しい手法を確立し、何を可能にしたかということです。

# Appendix

# References
