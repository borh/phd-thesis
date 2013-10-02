% Corrections for 'Contextually Aware Writing Assistance System for Japanese'
% Bor Hodošček
% \today

# Answers to questions received during public defense

## RQ 1 clarification \footnotesize{(Prof. Nakayama)}

**RQ 1**: Is it possible to utilize linguistic resources, such as corpora, to realize more effective systems for computer-assisted writing?

-   Compared to dictionaries and other forms of references, Natsume offers:
    1.  Far greater coverage of word combinations (collocations)
    2.  User-friendly visualization for large quantities of information
    3.  Allows users to 'discover' register differences (cf. RQ 2)
        -   Remaining issue: does this discovery process lead to deeper understanding of register?

\begin{tcolorbox}
\centering
\small
RQ1\&2 answered in Ch. 9: "Conclusion", pp. 99-101
\end{tcolorbox}

<!--
    Given that the process of L2 writing typically entails the user making use of various dictionaries and other forms of references, one may ask whether it is possible to utilize corpora to go beyond the inherent limitations associated with these time-tested tools.
    The type of corpus-driven writing assistance systems proposed in this thesis focus on helping L2 learners of Japanese find collocations suitable to their writing purposes.
    Formed from commonly cooccurring words, the number of possible collocations is far greater than the number of words themselves, and, thus, requires a different approach for the effective presentation of such quantities of information.
    The interfaces for Natsume provide user-friendly ways of visualizing the information content relating to collocations, by taking advantage of knowledge about the kinds of writing contexts that collocations commonly occur in.
    As a consequence, Natsume is able to provide a form of surrogate knowledge about register differences within Japanese for the L2 users.
    In this way, the system is effectively able to not only sidestep the problems that L2 learners face due to a lack of appropriate intuitions about register differences, but it also effectively offers richer learning opportunities for the users to make discoveries about collocations by themselves.

    Taking this concept even further, the Nutmeg system can detect register misuses relating to collocations within the user's writings.
    This approach allows the system to not only detect grammaticality issues, but also paves the way towards realizing a correction system for academic writing style.
-->

## RQ 2 clarification \footnotesize{(Prof. Nakayama)}

**RQ 2**: Is it possible to provide writing style guidance based on corpora alone?

-   Users explicitly instructed to prefer collocations from the STJC corpus were, in general, able to produce more appropriate collocations for the academic register
-   The user-led nature of Natsume is not enough to identify many register issues
    -   An automated checking system is necessary $\rightarrow$ Nutmeg
-   Remaining issue: Effective strategies for user error feedback (how to make writers reflect and improve their writing)

<!--
    Evaluations of Natsume revealed that when users have been explicitly instructed to prefer collocations that have higher frequencies within the STJC corpus, they are generally able to produce more appropriate collocations within their report writing and sentence rewriting.
    However, the gathered evaluations did not examine the possibilities of using the system to deepen learner understanding of L2 registers, so that remains an open question to be taken up in future studies.
    On the other hand, evaluations concerning the detection of register misuses relating to words and collocations within the Nutmeg system highlighted some interesting possibilities of providing writers with feedback about possible errors.
    Currently, the Nutmeg system provides indirect feedback about such possible learner errors, which can be beneficial in prompting the writer to reflect further on their writing.
    There are, however, still a number of unanswered questions that could be addressed.
    For instance, it would be interesting to investigate and compare which feedback strategies could be more effective, such as specific scaffolding strategies designed to guide users to appropriate decisions but to later gradually fade back as the learner gains deep insights into the mechanisms for their own mistakes.
-->

## Field of experience/context \footnotesize{(Assoc. Prof. Yamamoto)}

-   Clarified the relationships between field of experience and context (register, topic, and readability) in Schramm's model (pp. 12-15)
-   Discussion of field of experience included in other chapters
    -   Eventual goal of writing assistance: expansion of the writer's field of experience that enables them to write texts that are appropriate to the target L2 register
    -   Awareness in system $\rightarrow$ 'know' parts of the writer's field of experience, as well as that of the target audience

<!--
-   In this model, the intersection between the source and destination's respective fields of experience represents the common field of experience, which is the essential element for successful communication.
-   Given the definition of field of experience as the beliefs, values, experiences, and learned meanings of an individual [@schramm1955], clearly it is only possible for a signal to be successfully decoded when there is a significant degree of overlap between the respective fields of experiences that the source and destination bring to the communication.
-   In order to increase the possibility of being correctly understood in such situations, writers must seek to accommodate the reader and attempt to narrow the gap between their respective fields of experience in the only way possible---by expanding their own field of experience.
-   The constrained version of the communication model has several direct implications for the writer and their field of experience:
    -   The writer must consider the reader's perspective, which, within the model framework, refers to assuming, or targeting, to a certain level of knowledge on the part of the reader audience.
        Thus, the writer can only seek to convey information that falls within the field of experience that the readers are assumed to possess.
    -   Reflecting these assumptions, the writer must also employ appropriate scaffolding strategies, including their gradual removal, in order to facilitate the reader in reaching an appropriate interpretation of the writer's intended signal.
-   While the importance of the shared field of experience is clearly implied within Schramm's model of communication, this thesis specifically seeks to develop and elucidate the key notion of context that the shared field of experience represents, by focusing on the three contributing factors of register, topic, and readability.
-   At the heart of this thesis is a detailed examination of the shared field of experience proposed in @schramm1955's model of communication in light of the constrained model of communication presented in \Cref{fig:schr-o} and its reinterpretation in terms of a model of writing context.
-   As components of field of experience, register and topic are discussed again in \S\ref{sec:register} and \S\ref{sec:topic}, which explains how they can be indirectly measured from the linguistic features extractable from written text [cf. @Biber2009].
-   In terms of the constrained model of communication presented in \S\ref{sec:context}, while language-internal criteria roughly equates to the shared field of experience, the language-external criteria encompasses the wider range of factors that constrain the context under which communication can occur.
-   Another way of conceptualizing this awareness is as an expansion of the writer's field of experience that enables them to write texts that are appropriate to the target L2 register.
-   In a very real sense, the system would effectively _know_ part of the field of experience possessed by the writer, and given the system's _knowledge_ of the target audience, could also include some knowledge that reflects the field of experience possessed by the target audience.
-   The models of register, topic, and readability as major influencing components of the field of experience.
-->

<!--
1.  Schrammのfield of experienceを使っているが、intersectionが大きければ大きいほど、理解があると書いてある。その２つのフィールドが時代を超越してあったり、または専門が違っていたり、またはそれぞれの人間の？？が違っていたりすることで理解が得られないということ。field of experienceの中を深めてその中のsignalについて、レジスターに関する要素が、sharedすればするほど理解度が大きい、そして同じようにトピックがある。そのschemaについて、レジスター的なFOEがある、そしてトピックとしてみたFOEがある、が、signalそのものは変わらない？レジスター、トピックなどはFOEの一つの見方なのでしょうか（はい。）。
    -   the lines from register/topic/... shared FOE look like they point to the signal, while they should only point to the highlighted area.

2.  単なるシグナルを教えるだけでは、どうしようもないレベルで、レジスターのようなもののed areaを広げていくとか、トピックに関するshared areaを広げていくことを組み合わせるものとして、この研究が始まったのかな。その研究の一環として一つはレジスターを深めたという考え方でよろしいでしょうか？WriterとReaderのレジスターを分離して考えるというアプローチはありませんでしたか？
-->

## Effects of corpora \footnotesize{(Prof. Nakayama)}

1.  \underline{Scientific and Technical Japanese Corpus} (STJC)
    -   Target register for L2 writers in academic contexts
    -   Users of Natsume able to directly refer to it for information about collocations

2.  Register misuse identification method + models of register and topic
    -   Relies on differences within various corpora---improves with access to more topics and registers (more corpora)


<!--
The largest contributing corpus is undoubtedly the Scientific and Technical Japanese Corpus (STJC) introduced in \S3.1, as it represents the target register of L2 writers in academic contexts.
Evaluations of Natsume revealed that when users have been explicitly instructed to prefer collocations that have higher frequencies within the STJC corpus, they are generally able to produce more appropriate collocations within their report writing and sentence rewriting.
However, the register identification method in \S8.2.1 gains much of its predictive strength from the inclusion of many corpora that contain contrasting registers.

どういったコーパスが効果をもたらしている？そのコーパスのどのような性質が関わるか？
-->

## Readability model (1) \footnotesize{(Assoc. Prof. Akama)}

\small

Table: \small{Textbook media by grades and school (Table 18, pp. 50).}\label{tab:r:grades}

**School**  **Grade**   **Sentences**  **Paragraphs**  **Samples**
----------- ---------- -------------- --------------- ------------
Elementary  1                     363             121            9
            2                     505             173           10
            3                   1,492             460           19
            4                   1,418             414           15
            5                   2,228             552           20
            6                   3,340             888           21
Middle      7                   1,570             523           14
            8                   5,172           1,149           29
            9                   4,438           1,056           24
High        10                 32,926           6,744          251
            TOTAL              53,513           9,750          412


\vspace*{-.8em}

-   Maintained similar population levels for training and validation using stratified random split strategy
-   Consider down-sampling strategies for future studies

<!--
    -   A table showing the original data distribution between grades and school levels is presented in Table 18 (pp. 50).

    -   The previous analysis was not clear enough in mentioning that the process of recoding to school levels was intended to bring the school level population levels closer.
        The remaining imbalances were taken into consideration when constructing the training and test sets, by using a stratified random split strategy based on school level to maintain class distributions between the training and test sets similar.
        Finally, other possible remedies to the class imbalance problem, including down-sampling and the setting of prior model probabilities, were mentioned as possible avenues for exploration in future work (pp. 60).
-->

## Readability model (2) \footnotesize{(Assoc. Prof. Akama)}

-   `glmnet` (multinomial regression) model originally used for its automatic feature selection feature
-   Addition of glmnet `SVM`, `random forest`, `C5.0`, and `neural net` models to analysis (pp. 53-54)
    -   Results improved only at the sentence level compared to `glmnet`
    -   Overall, distribution of misclassifications worst for `glmnet` model
        -   Possibly more interpretable than the others

<!--
    The use of the multinomial regression model (glmnet) was explained in terms of its relative robustness against collinearity problems and inclusion of automatic feature detection.
    In the revised thesis, the glmnet model was also compared to 4 other, perhaps more conventional, models: SVM, random forest, C5.0, and neural nets (pp. 53-54).
-->

## Readability model (3) \footnotesize{(Assoc. Prof. Akama)}

Training and validation

-   The exact training and validation process was explained in terms of Algorithm 1 (pp. 55)
-   Various definitions of model performance statistics (i.e. the 95% confidence interval for the model accuracy based on CV) given (pp. 55)
-   Exploration of training and test set split ratios other than the 3:1 left for future work (pp. 60)

<!--
### (Assoc. Prof. Akama)

1.  サンプル母集団の解説の修正
    -   Readability (30-32ページの機械学習に関して)
        -   Why is the training and testing set proportion 75%:25%?
        -   What is the significance level of the accuracy/Why did you support a very strong hypothesis based on the population level?
            -   It comes from 10-fold cross-validation.
            -   It measures variability in the model(!).
        -   What is the distribution of the population level used in the machine learning?
        -   What is the reason for using glmnet vs. other techniques such as SVM, multinomial distribution model using multiple comparison correction like the Bonferroni correction (or the ... ...), because the size of the three groups are quite different; it would be better to run a permutation test using a multiple comparison ... method.
        -   Slide 42の最初のポイントと図の関係を明示的にすることで、混乱を防ぐ
            -   Just need to be more clear here and fix p. 59 / 60 in the paper ('scores' can refer to Natsume and Control, but in this case really refer to pre-test scores). The ref and label need to be fixed to refer to the right results.

## Answer

1.  Resampling

    Cross-validation vs. permutation tests.
    75:25 train/test data split (I should have used held-out data).
-->

## Instructions given during experiment \footnotesize{(Prof. Nakayama)}

\vspace*{-1em}

-   All instructions to participants during both experiments were given in Japanese.
-   The thesis provides copies of tasks for both Experiment 1 and Experiment 2 in the Appendix (\S10.2-3, pp. 109-112).

-   The experimental setup for Experiment 1 (sentence rewriting task) provided in \S7.5.1.1 (pp.68-70)
-   That for Experiment 2 (report writing task) detailed within \S7.5.2.1 (pp.75-76).

\begin{tcolorbox}
\small
In both cases, participants were explicitly instructed to prefer collocations that have higher frequencies within the STJC corpus.
\end{tcolorbox}


<!--
### Experiment 1 (Sentence rewriting task: \S7.5.1.1, pp. 68-70)
-->

<!--
-   Participants were allotted 30-60 minutes to complete each task.
-   Use of electronic and online dictionaries^[Dictionaries were restricted to non-scientific and technical Japanese, i.e. general Japanese-Japanese and L2 learner dictionaries.] was permitted during the tasks, and most participants made use of them.
-   Participants were instructed in the use of Natsume for 5 to 10 minutes prior to commencing the treatment task.
-   For both tasks, the participants were instructed to rewrite the sentences into an academic style.
    During the control phase, participants had to rely solely on their intuitions about academic style.
    During the treatment phase, the participants were instructed to look at the STJC genre frequency when deciding on about the appropriateness of expressions for academic writing.
-->

<!--
### Experiment 2 (Report writing task: \S7.5.2.1 pp. 75-76)
-->


<!--
-   The participants were provided with laptops, wrote in MS Word 2010, and used the Firefox 5 browser (when using Natsume).
-   The participants had to write for at least half an hour but no longer than one hour.
-   In their reports, they had to decide to either reject or agree with the theme and to back up their decision with reasoning.
    A short summary of the topic for each theme was provided and is available in Appendix \S10.3.1.
-   Each report had to be at least 200 characters long.
-   Use of the /de-aru/ form was mandated.
-   When using Natsume, the participants would refer to the STJC genre frequency when deciding if a collocation was suitable for the report.
-   Use of general, non-specialized electronic or online dictionaries was allowed for both conditions (control and treatment).
-   Before the experiment, all participants were introduced to Natsume and trained in how to used it for 5-10 minutes.
-->

## Linear regression in Experiment 1 \footnotesize{(Prof. Nakayama)}

\vspace*{-1em}

-   New analysis of scores: conducted COANOVA with L1 as the covariate, and condition, test, and group as independent variables
    -   Main effect for condition (\*\*\*) and L1 (\*) found
-   Post-hoc comparisons using the Tukey HSD test
    -   **Condition**: treatment > control (by 10.51 points, $p = .0005$)
    -   **L1**: no significant differences between Mandarin, Korean, and Other found (below the $p<.05$ level)
-   More examination of L1 issues necessary


<!--
Factor & Comparison & $\mu_1-\mu_2$ & Lwr bound & Upr bound & $p_{adj}$
\\
\midrule
L1 & Mandarin-Korean & 0.39 & -8.10 & 8.88 & 0.9934
\\
& Other-Korean & 8.45 & -1.35 & 18.25 & 0.1047
\\
& Other-Mandarin & 8.06 & -0.42 & 16.55 & 0.0661
\\
Condition & Treatment-Control & 10.51 & 4.74 & 16.28 & 0.0005
\\
\bottomrule
\end{tabular}
\end{table}
\end{multicols}
-->

\begin{tcolorbox}
\centering
\small
The results are available in \S7.5.1.3 (pp. 71-72).
\end{tcolorbox}

## Generality \footnotesize{(Prof. Nohara)}

-   The methods and systems proposed are based on **comparisons** between corpora (general)
-   Focus on academic paper writing for L2 Japanese writers (specific focus)

-   Generality of collocations relating to differences in association strength within different registers
    -   All collocation frequency and association strength scores are based on their actual appearance in corpora $\rightarrow$ if association strength is weaker, then the scores will be lower
    -   Differences in association strength between corpora are a function of the register and topic of the corpus
    -   Caveat: need to have access to target writing corpus

<!--
    However, the overriding theme within the thesis that specifically targets L2 writers of Japanese, that are writing reports or papers in Japanese, somewhat limits the discussion for other types of writers and target registers.

-   My view on the fact that collocations from different registers differ in association strength is that this is a problem stemming not just from the viewpoint of register, but also from the viewpoint of topic.
    In order to offer any conclusive answers on this topic would then require knowing: (1) the inter- and intra-corpus variability in registers, (2) the inter- and intra-corpus variability in topics.

-   Finally, the generality problem mostly stems from (1) pedagogical reason that limit discussion on L2 writers of Japanese in an academic context, and (2) practical reasons involving the limited availability of corpora for specific writing domains such as e-mail.
-->

<!--
-   The association strength of collocations per register is probably a function (or at least affected by it) of the inter- and intra- variability in registers and topics per corpus. Possible ways to see differences here is to compare collocation measure scores and average collocates per word by corpus (ltree) and see how much of an effect this could have. Also need to find some research to even back Prof. Nohara's statement, though it seems reasonable. We should watch out for similar text length vocabulary changes too (maybe Yule's k?).
-   The generality is limited by the need for a target corpus that aligns with the writer's target area (in register, topic and readability).
    -   Pedagosko predstavljen problem: zato imamo en korpus.

------

Operacijsko definirani modeli realnosti.
Kaj je pa realnost?
-->

<!--
# Major thesis changes: New materials

## Chapter deletion

-   Chapter 7 was originally planned to give an overview of all systems, but as the introductions to the Natsume and Nutmeg systems were sufficiently clear in their respective chapters, the need for this chapter was lost.
-   Chapter 10 featured some proposals for an integrated system. These proposals were rather moved to the conclusion chapter.

Additionally, the following sections were moved (not shown in the Figure):

-   The introduction to register previously available in the register chapter (\S4.2) was moved to chapter 2 (\S2.2), where more connections to the field of experience and language variation could be better explored.
    Consequently, chapter 4 now focuses on the MVR.
-   The register identification method previously included at the end of the register chapter (\S4.2) was moved to the Nutmeg chapter (\S8.2.1), where it is also evaluated.

Finally, the Appendix was reworked to include only necessary information.

## Chapter 2: Contextual Model and Writing Context

This chapter was expanded to include four new sections focusing on various approaches to the modeling of language variation within linguistics:

-   Register and Context (pp. 14-16)

-   Systemic Functional Linguistics (SFL) (pp. 16-18)

-   Multi-Dimensional (MD) Approach (pp. 18-19)

-   Summary (pp. 20-21)


## Chapter 5: Topic Model

This chapter was expanded with new data and analysis:

-   Results (pp. 42-44)

    The analysis of correlation results was expanded, and a hierarchical cluster analysis was performed on the variety of topics contained within each media.

-   Discussion (pp. 44-46)

    The discussion reviewed the results of the previous section by examining commonalities with the top five topics generated for each media.

-   Conclusion and Future Work (pp. 46-48)

## Chapter 7: Natsume

The Natsume chapter was expanded with more detailed discussion and data.

-   Experiment 2 survey

    Results from the post-experiment survey (Figure 30, pp. 83; discussion on pp. 81, 84) revealed slightly worse attitudes towards use of Natsume being tiring.
    In order to investigate these results, a multiple linear regression was performed (Table 32, pp. 84) on the time taken to complete the writing task.
    While the effect of the treatment condition was not found to be statistically significant, the effect of theme was found to have led to a statistically 5.77 minute longer time when writing on theme 2.
-->
