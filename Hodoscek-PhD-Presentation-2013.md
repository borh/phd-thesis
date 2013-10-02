% Contextually Aware Writing Assistance System for Japanese
% Bor Hodošček
% 2013/6/18

# Background (Part I)

## Introduction (Ch. 1)

\note{

Color scheme:
Color Palette by Color Scheme Designer
Palette URL: http://colorschemedesigner.com/#0c31Tvnw0w0w0
Color Space: RGB;
*** Primary Color:

   var. 1 = #FF4105 = rgb(255,65,5)
   var. 2 = #BF5433 = rgb(191,84,51)
   var. 3 = #A62902 = rgb(166,41,2)
   var. 4 = #FF7144 = rgb(255,113,68)
   var. 5 = #FF9776 = rgb(255,151,118)

*** Secondary Color A:

   var. 1 = #0C6BA2 = rgb(12,107,162)
   var. 2 = #255A7A = rgb(37,90,122)
   var. 3 = #04446A = rgb(4,68,106)
   var. 4 = #409BD1 = rgb(64,155,209)
   var. 5 = #66A9D1 = rgb(102,169,209)

*** Secondary Color B:

   var. 1 = #76E605 = rgb(118,230,5)
   var. 2 = #6EAC2E = rgb(110,172,46)
   var. 3 = #4C9501 = rgb(76,149,1)
   var. 4 = #9AF240 = rgb(154,242,64)
   var. 5 = #B2F270 = rgb(178,242,112)

\footnotesize
My name is Bor Hodošček and I would like to talk about the present state of my PhD thesis titled: Contextually aware writing assistance system for Japanese.

First, I would like to present the outline of my thesis, which consists of four chapters.
As my research touches on several different academic fields such as linguistics, natural language processing and educational technology, the introduction and literature review in Chapter 1 will provide the necessary background for the succeeding chapters.

Chapter 2 will introduce the model of context, which consists of three models: the register model, then the topic model, and finally the readability model.

In the next chapter, Chapter 3, entitled writing assistance system, I will introduce two writing assistance systems developed in collaboration with other researchers as marked in the slide.
The first writing assistance system is called Natsume, while the second, made to cover some shortcomings in the first, is called Nutmeg.
Finally, a system that encapsulates the models listed in chapter 2 will be proposed.

**Something about why/how the new system is significant**

Chapter 4 will conclude my thesis.
}

### Writing and Communication

\vspace{-.7em}

![Adapted from @schramm1955's communication model](images/schramm-original-model.pdf)


\begin{tcolorbox}
\centering
A \textbf{common field of experience} is essential.
\end{tcolorbox}

\note{
\footnotesize
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
-   best writing assistance: writing centers in the US?? staff talks through the essay with the writer, in a tight feedback loop (check \parencite{Bawarshi2010})

-   what is the minimum language proficiency required to make use of writing assistance systems?
}

### Computer-Aided Writing Assistance

<!--
\vspace{-1em}

-   Online dictionaries
-   Spell checkers
    -   No equivalent for Japanese, because of prevalence of smart Input Method's such as Google IME
-   Grammar checkers (for Japanese)
    -   Effective in specific domains in English [@hoard1992automated], or specific sub-set of grammar such as case-particle misuse [@Mizumoto2012E]
-   Style checkers (for Japanese)
    -   Prescriptive style manuals; Yahoo! Japan's [_Kousei shien_](http://developer.yahoo.co.jp/webapi/jlp/kousei/v1/kousei.html) service

The following section introduces various methods for computer-aided writing assistance with a particular focus on those targeting the Japanese or semantic errors [@naber2003rule].
-->

Table: Error assistance types.\vspace{-1em}

---------------------------------------------------------------------
**Error type** **Tools employing these techniques**
-------------- ------------------------------------------------------
Spelling       Word Processor, Web Browser, IME (Japanese)

Grammar        Word Processor (limited support in MS Word)

Style          'After the Deadline' [@Mudge:2010:DPS:1860657.1860661]
---------------------------------------------------------------------

\vspace{-.5em}

\begin{tcolorbox}
Increasing trend to leverage large-scale language data for automated writing assistance.
\end{tcolorbox}

\note{
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
-   Grammar vs. style checkers (cf. \parencite{heidorn2000intelligent})
    -    Domain-specific grammar checkers can be effective (cf. Boeing's \parencite{hoard1992automated}), but require considerable manual tuning and rule creation
-   Direct or indirect feedback?
    -    Indirect feedback preferred because it forces the writer to reflect [@godwin2008emerging]

-   what are the main evolutions (revolutions) in writing on a computer compared to, say, a typewriter or pen?
-   similar systems (feature matrix?)
    -   Newer efforts: Coori, lang-8
-   domain-specific grammar checkers have been found to be effective (cf. Boeing's \parencite{hoard1992automated}) provided they encode domain-specific rules into the engine, which is time-labor intensive

> What tends to be of most use to learners is indirect feedback, which points to problems in written
> work but leaves it to the writer to find the solution. This requires the learner to reflect on the
> application of language rules to one's own actual writing. Many language teachers use codes (such
> as John Lalande's ECCO - error correction code) to mark student writing. -- \parencite{godwin2008emerging}

: Feature matrix

Feature                  System 1  System 2
----------------------- --------- ---------
Spelling correction(*)
Thesaurus
Collocation checking
----------------------- --------- ---------

*: Spelling correction makes less sense in Japanese than for some other languages; the IME prevents many errors.

-   put all systems along writing assistance vs. general L2 learning systems axes?
}

### Research Questions

**Research Question 1**

> Can linguistic resources such as corpora be used to make computer-assisted writing more effective?

**Research Question 2**

> Is it possible to correct writing style using only corpora?

### Research Aim and Approach

\vspace*{-.5em}

\begin{tcolorbox}[title={Research Aim}]
Construction and evaluation of writing assistance system for Japanese based on the concept of writing context.
\end{tcolorbox}

\begin{tcolorbox}[title={Approach}]
\begin{enumerate}
  \item Quantitative exploration of language data $\rightarrow$ construct models of language.
  \item Construction of writing assistance system, iterating on system design based on evaluation experiments.
\end{enumerate}
\end{tcolorbox}

<!--

### Research Aim

Construction:

-   Models of context **(Ch. 2)**
-   Web-based writing assistance system **(Ch. 3)**

Evaluation:

-   Evaluate models of context **(Ch. 2)**
-   Evaluate system features  **(Ch. 3)**

\note{
Finally, the aim of my research is to construct and evaluate a writing assistance system for Japanese based on the concept of writing context.

With respect to construction, I am referring to both the construction of the model of context in Chapter 2, as well as the construction of a web-based writing assistance system in Chapter 3.

With respect to evaluation, I am referring to the evaluation in of the models of context in Chapter 2, as well as the evaluation of the system in Chapter 3.
}

-->

# Contextual Model (Part II)

## Con. Model and Writing Con. (Ch. 2)

### Con. Model and Writing Con. (Ch. 2)

\centering
\includegraphics[height=.8\textheight]{images/phd-chapter-outline-ch2.pdf}

### Register, Topic and Readability

\vspace*{-.6em}

\begin{tcolorbox}[title={Register}]
Variation in language directly connected with the situation, or context, of its use.
\end{tcolorbox}

\begin{tcolorbox}[title={Topic}]
The subject(s) of a text (one or more topics per text).
\end{tcolorbox}

\begin{tcolorbox}[title={Readability}]
A quality of text that makes it easy or hard to understand.
\end{tcolorbox}

### Field of Experience

\vspace*{-.2em}
\centering
\includegraphics[height=.8\textheight]{images/schramm-model-new.pdf}

\note{
!!! FIX と→て
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

**The problem with words and, by extension, collocations, is that they are not purely topical or purely functional --- need both to assess correctly.

}

<!--
### Register and Topic

![Example of differences in register with same topic.\label{om-ex}](images/om-example.pdf)

-->

## Context and Corpora (Ch. 3)

### Context and Corpora (Ch. 3)

\centering
\includegraphics[height=.8\textheight]{images/phd-chapter-outline-ch3.pdf}

### Context and Corpora

\vspace{-.5em}

-   Data-driven approach to writing assistance where **context is modelled on differences in corpora**.
-   Multiple corpora varying in register, topic and readability.


1.  Scientific and Technical Japanese Corpus (STJC)
2.  Balanced Corpus of Contemporary Written Japanese (BCCWJ) ― contains 10 sub-corpora
3.  Japanese Wikipedia
    -   Included for its size (416m tokens).

\note{

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

}

### STJC

Table: Composition of STJC.\label{stjs-comp}

**Journal**                       **Tokens**  **Sources**
------------------------------- ------------ ------------
J. of Natural Lang. Proc.          1,655,975          201
J. Chem. Soc. of Japan               708,269          184
J. Inst. of El. Eng. of Japan A      640,259          163
J. Japan Soc. of Civil Eng. D        389,182           41
J. Inst. of El. Eng. of Japan B      241,303           50
J. Japan Soc. of Civil Eng. C        159,338           21
J. Japan Soc. of Civil Eng. A        156,644           34
J. Japan Soc. of Civil Eng. B         84,234           21
J. Nippon Med. Sch.                   66,885           28
TOTAL                              4,102,089          743


### BCCWJ

\vspace{.2em}

Table: BCCWJ top-level metadata label statistics.\label{bccwj-t}

**Code**  **Metadata**           **Tokens**  **Sources**
--------- ------------------- ------------- ------------
PB+LB+OB  Books                  70,472,742       22,058
OY        Yahoo! Blogs           13,212,757       52,676
OC        Yahoo! Q&A             12,088,127       91,445
OM        Minutes of the Diet     5,600,649          159
OW        White papers            5,495,254        1,500
PM        Magazines               5,114,752        1,996
OP        Gov. pamphlets          4,739,306          354
OL        Legal documents         1,206,481          346
OT        Textbooks               1,126,214          412
PN        Newspapers              1,036,285        1,473
OV        Verse                     237,685          252
TOTAL     11                    120,330,252      172,671

<!--

## Units of Language

### Units of Language

Japanese employs four scripts:

-   Kanji: 漢字
-   Hiragana: ひらがな
-   Katakana: カタカナ
-   Rōmaji: MOTTAINAI, MEXT

In the context of natural language processing, the units of Japanese can further be expressed in terms of:

-   Short Unit Words (SUW): ホテル | を | 使っ | て | 大型 | 夜景 | 鑑賞 | イベント | を
-   Long Unit Words (LUW): ホテル | を | 使っ | て | 大型夜景鑑賞イベント | を
-   Chunks: ホテルを | 使って | 大型夜景鑑賞イベントを

-->

## Register Model (Ch. 4)

### Register Model (Ch. 4)

\centering
\includegraphics[height=.8\textheight]{images/phd-chapter-outline-ch4.pdf}

<!--
### Register Model

**Register definition:** _variation in language directly connected with the situation, or context, of its use._

Examples

-   Spoken vs. written language
-   Formal, academic prose vs. informal, casual prose

\begin{tcolorbox}[title=Proposed models]
N-gram language model, functional word model, tf-idf ($\rightarrow 0$) vector space model
\end{tcolorbox}

**Outcome**: Infer the register of a text.

\note{
Manifestation in language:

-   Register can be quantified by comparing corpora (databases containing collections of text) belonging to different genres [@ALAHodoscek2011]

Proposed Model:

-   Compare existing models and choose the best one (tf-idf based, word class based, \ldots)

-   \parencite{ALAHodoscek2011} (refereed)

    How to tie this in with my final model: emphasize the theory behind the method, it was a stepping stone to other models

-   Master's thesis

    The arbitrary separation of functional and content words was useful, but neglected to take into account differences in topic distributions between genres
}

\note{
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
    -   how to fix the high correlation scores????
}

-->

### Register Model

\begin{tcolorbox}[title=Definition]
Variation in language directly connected with the situation, or context, of its use.
\end{tcolorbox}

\begin{tcolorbox}[title=Goal of Model]
By measuring differences in register between different corpora in the BCCWJ, make it possible to offer a quantitative explanation of register.
\end{tcolorbox}


### Register Model: Modifier-Verb Ratio

Method first proposed by @Kabashima65 to classify texts into descriptive and summative categories based on word-class ratios:

\vspace*{-.8em}

\begin{figure}
\centering
\begin{tikzpicture}[grow=right]
\tikzset{edge from parent/.style={thick,
draw,
    edge from parent path={(\tikzparentnode.east)
    -- +(0,0pt)
    |- (\tikzchildnode)}}}
\tikzset{level distance=130pt,sibling distance=12pt}
%\tikzset{execute at begin node=\strut}
\Tree [.text [.summative(N=high) ] [.descriptive(N=low) [.static(MVR=high) ] [.active(MVR=low) ] ] ]
\end{tikzpicture}
\caption{Categorization of texts using noun and modifier-verb ratios.}
\label{MVRfig}
\end{figure}

\vspace*{-2em}

$$\text{MVR} = 100 \frac{\text{ratio of modifiers in text}}{\text{ratio of verbs in text}}$$


### Bagplots of BCCWJ (MVR=low)

\vspace*{-2em}
\centering
\begin{figure}
\includegraphics[height=1.1\textheight]{images/mvr-1.png}
\caption{First group with small bag areas. Results are similar to \autocite{Kabashima65}: \textbf{negative correlation} between N and MVR.}
\end{figure}

### Bagplots of BCCWJ (MVR=high)

\vspace*{-1.8em}
\centering
\begin{figure}
\includegraphics[height=1.1\textheight]{images/mvr-2.png}
\caption{Larger bag areas. Magazines showed weak \textbf{positive correlation} between N and MVR which is unaccounted for in \autocite{Kabashima65}.}
\end{figure}

### Register: Summary

\vspace*{-.5em}

\begin{tcolorbox}[title={Summary}]
\begin{itemize}
\item Identified metadata with similar registers in the BCCWJ.
\item Identified metadata that should be handled with care: Yahoo! Blogs and Q&A have many small samples.
\end{itemize}
\end{tcolorbox}

\vspace*{-.5em}

\begin{tcolorbox}[title={Problems}]
Only one method of register identification explored: future models should include other measures (modality, language models, etc.).
\end{tcolorbox}

<!--
### Register

\begin{tcolorbox}[title={Summary}]
\begin{itemize}
\item Bottom-down orientation of bag confirmed.
\item Summative: White papers, Newspapers, and Textbooks.
\item Books has an average noun ratio, but higher than average modifier-verb ratio.
\item Yahoo! Blogs and Yahoo! Q&A: Great variation on descriptive-summative scale.
\item Magazines: High N, high MVR pattern not accounted for in previous research.
\item Some sample sizes are too short for reliable feature extraction and classification.
\end{itemize}
\end{tcolorbox}
-->

## Topic Model (Ch. 5)

### Topic Model (Ch. 5)

\centering
\includegraphics[height=.8\textheight]{images/phd-chapter-outline-ch5.pdf}


<!--
### Topic Model

**Topic definition:** _the subject of a text. Does not necessarily refer to the subject of a sentence. One or more topics per text._

\begin{tcolorbox}[title=Proposed models \parencite{NCHodoscek2012E}]
Probabilistic topic model (Latent Dirichlet Allocation), tf-idf ($\rightarrow max$) vector space model
\end{tcolorbox}

**Outcome:** Infer the topics of a text.

\note{
-   same as previous (LDA), or maybe DMR (Dirichlet-Multinomial Regression: using genre labels as features)
    -    one model per corpus or one big model?

-   Investigated relation between sub-corpora of the BCCWJ $\rightarrow$ topic $\ne$ register
-   Proposed Models


-   find topics which tend to appear in only one genre -- i.e. check the genre distribution of topics
-   check collocation/word's topic distribution and compare it to the register distribution
}

-->

### LDA Topic Model (1)

<!--
\vspace*{-.4em}

![LDA plate model used in \cite{NCHodoscek2012E}.](images/lda-topic-model.pdf)

-->

\begin{tcolorbox}[title={Model}]
Latent Dirichlet Allocation
\end{tcolorbox}

-   An LDA model infers a probabilistic mixture of topics per documents.
-   A topic is a probabilistic mixture of words.

\vspace*{-1em}

![](images/topic-model-1.pdf)

### LDA Topic Model (2)

![Each document has several topics assigned to it with given probability.](images/topic-model-2.pdf)

\note{
Proposed Model:

-   same as previous (LDA), or maybe DMR (Dirichlet-Multinomial Regression: using genre labels as features)
    -    one model per corpus or one big model?

-   find topics which tend to appear in only one genre -- i.e. check the genre distribution of topics
-   check collocation/word's topic distribution and compare it to the register distribution
}


### BCCWJ Topic Correlations (1)

<!--
\tiny
\begin{longtable}[c]{lrrrrrrrrrrrr}
\caption{Correlations between topics in sub-corpora.}\\
\toprule
   & PB   & LB   & OB    & PM    & PN   & OC    & OY    & OW    & OV    & OT   & OP    &  OL  \\
\midrule
%PB&      &      &       &       &      &       &       &       &       &      &       &      \\
LB & 0.85 &      &       &       &      &       &       &       &       &      &       &      \\
OB & 0.50 & 0.66 &       &       &      &       &       &       &       &      &       &      \\
PM & 0.58 & 0.56 &  0.43 &       &      &       &       &       &       &      &       &      \\
PN & 0.56 & 0.55 &  0.29 &  0.59 &      &       &       &       &       &      &       &      \\
OC & 0.25 & 0.18 &  0.28 &  0.54 & 0.33 &       &       &       &       &      &       &      \\
OY & 0.18 & 0.22 &  0.34 &  0.60 & 0.37 &  0.77 &       &       &       &      &       &      \\
OW & 0.33 & 0.17 & -0.09 &  0.10 & 0.49 &  0.06 & -0.11 &       &       &      &       &      \\
OV & 0.28 & 0.42 &  0.42 &  0.27 & 0.16 &  0.16 &  0.33 & -0.20 &       &      &       &      \\
OT & 0.52 & 0.54 &  0.35 &  0.34 & 0.38 &  0.19 &  0.20 &  0.24 &  0.29 &      &       &      \\
OP & 0.14 & 0.09 & -0.02 &  0.17 & 0.37 &  0.10 &  0.13 &  0.29 & -0.01 & 0.13 &       &      \\
OL & 0.24 & 0.04 & -0.15 & -0.08 & 0.29 &  0.04 & -0.17 &  0.61 & -0.22 & 0.12 &  0.23 &      \\
OM & 0.18 & 0.10 & -0.04 & -0.01 & 0.36 & -0.03 & -0.15 &  0.53 & -0.18 & 0.08 &  0.21 &  0.56\\
\bottomrule
\end{longtable}
-->

\begin{longtable}[c]{lrrrrrrr}
\caption{Correlations between topics in sub-corpora.}\\
\toprule
   & PB   & LB   & OB    & PM    & PN   & OC    & OY    \\
\midrule
LB & \bfseries 0.85 &      &       &       &      &       &       \\
OB & \bfseries 0.50 & \bfseries 0.66 &       &       &      &       &       \\
PM & \bfseries 0.58 & \bfseries 0.56 &  0.43 &       &      &       &       \\
PN & \bfseries 0.56 & \bfseries 0.55 &  0.29 & \bfseries 0.59 &      &       &       \\
OC & 0.25 & 0.18 &  0.28 & \bfseries 0.54 & 0.33 &       &       \\
OY & 0.18 & 0.22 &  0.34 & \bfseries 0.60 & 0.37 & \bfseries 0.77 &       \\
OW & 0.33 & 0.17 & -0.09 &  0.10 & 0.49 &  0.06 & -0.11 \\
OV & 0.28 & 0.42 &  0.42 &  0.27 & 0.16 &  0.16 &  0.33 \\
OT & \bfseries 0.52 & \bfseries 0.54 &  0.35 &  0.34 & 0.38 &  0.19 &  0.20 \\
OP & 0.14 & 0.09 & -0.02 &  0.17 & 0.37 &  0.10 &  0.13 \\
OL & 0.24 & 0.04 & -0.15 & -0.08 & 0.29 &  0.04 & -0.17 \\
OM & 0.18 & 0.10 & -0.04 & -0.01 & 0.36 & -0.03 & -0.15 \\
\bottomrule
\end{longtable}

### BCCWJ Topic Correlations (2)

-   Books
    -   Bestsellers (OB) not as close in topic as Publication (PB) and Library (LB)
    -   In general, topic fit with Yahoo! Blogs (OY) and Q&A (OC) is low, though Bestsellers closer in topic.
-   Magazines
    -   Closer to Internet (OY and OC) corpora than others.
-   Yahoo! Blogs and Q&A
    -   Low correlation except with each other and Magazines.
-   White papers
    -   Closest to Newspapers (PN) in topic, but see next slide.

### BCCWJ Topic Correlations (3)

\begin{longtable}[c]{lrrrrr}
\caption{Correlations between topics in sub-corpora (cont.).}\\
\toprule
   & OW    & OV    & OT   & OP    &  OL  \\
\midrule
OV & -0.20 &       &      &       &      \\
OT &  0.24 &  0.29 &      &       &      \\
OP &  0.29 & -0.01 & 0.13 &       &      \\
OL &  \bfseries 0.61 & -0.22 & 0.12 &  0.23 &      \\
OM &  \bfseries 0.53 & -0.18 & 0.08 &  0.21 &  \bfseries 0.56\\
\bottomrule
\end{longtable}


\begin{tcolorbox}[title={Summary}]
Minutes of the Diet vs Legal documents/White papers: corpora that \textbf{vary in register}, but are \textbf{close in topic}.
\end{tcolorbox}

<!--
\vspace{-1em}
\begin{center}
\includegraphics[height=.9\textheight]{images/topic-corr.png}
\end{center}
-->

## Readability Model (Ch. 6)

### Readability Model (Ch. 6)

\centering
\includegraphics[height=.8\textheight]{images/phd-chapter-outline-ch6.pdf}

### Readability Model

\begin{tcolorbox}[title=Definition]
A quality of text that makes it easy or hard to understand.
\end{tcolorbox}

\begin{tcolorbox}[title=Goal of Model]
Use a combination of vocabulary, collocation, syntactic structure features to predict the readability of sentences and texts.
\end{tcolorbox}

<!--
**Outcome:** Grade readability of text, sentences, collocations and words.
-->

\note{

Readability is the result of interaction between the text (content, style, design, ...) and the reader (prior knowledge, reading proficiency, motivation, ...).

Readability as aspect of context.

Readability at the micro and macro scales:

-   micro: sentence readability
-   macro: logical structure readability

Why do we focus on the micro?
What are the problems with extending the micro readability measures to the macro scale?
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

-   \parencite{CASTELJHodoscek2012}
-   JLPT word list
-   BCCWJ word list (Matsushita TM list (Tokyo Univ.): [日本語を勉強する人のための語彙データベース](https://www.google.co.jp/url?sa=t&rct=j&q=&esrc=s&source=web&cd=1&cad=rja&ved=0CC4QFjAA&url=http%3A%2F%2Fwww.wa.commufa.jp%2F~tatsum%2FVDLJ_Ver1_0_International-Students.xlsx&ei=owAaUfOXDO_vmAXvmoHwDA&usg=AFQjCNHMEPokeGPt7vQlSf-J78ZxHcXhsg), Tsukuba Univ. list: [日本語教育語彙表](http://kotoba.nuee.nagoya-u.ac.jp/jc2/base/))
-   Obi2
}


### Surface Features of Text

\begin{center}
\includegraphics[height=\textheight]{images/readability-surface.pdf}
\end{center}


### Syntactic Features of Text

\centering
\includegraphics[height=1.1\textheight]{images/readability-syntactic.pdf}

### Results: Feature Correlations

\small


Table: Correlations of linguistic features with Textbook grade levels.

**Level**      **Factor**              **Sentence**    **Paragraph**       **Sample**
-------------- ------------------- ---------------- ---------------- ----------------
Writing system Hiragana            \bfseries -0.334 \bfseries -0.470 \bfseries -0.720
               Katakana                       0.091            0.142            0.168
               Kanji               \bfseries  0.331 \bfseries  0.443 \bfseries  0.730
               Rōmaji                         0.067            0.145            0.153
               Symbols                       -0.071           -0.056           -0.373
               Commas                        -0.047           -0.114           -0.028
Surface        Characters                     0.206            0.147            0.334
               Tokens              \bfseries  0.209            0.303            0.589
               Chunks                         0.201            0.290            0.597
Syntactic      Link distance                  0.174            0.302 \bfseries  0.631
               Chunk depth                    0.182 \bfseries  0.311            0.606
               Predicates                     0.126            0.190            0.544
Vocabulary     JLPT level                    -0.206           -0.169           -0.283
               BCCWJ-LB level                -0.154           -0.185           -0.301


### Results: glmnet Model (1)

\begin{tcolorbox}[title={glmnet}]
\small
Lasso and elastic-net regularized generalized linear models package for R.
\end{tcolorbox}

<!--
Using the `glmnet` package for R, we constructed a generalized linear model of readability in the Textbook sub-corpus (lambda chosen using 10-fold cross validation with the `caret` package for R).
Because of the small amount of data available for grades 1-9, we chose to group grades into three categories: elementary school (G1-6), middle school (G7-9), and high school (G10-12).
In addition, the Textbook sub-corpus was partitioned into training and test sets (75%:25%) containing equivalent proportions of G1-6, G7-9 and G10-12 observations for model evaluation purposes (Table \ref{r:tt}).
-->

Table: Textbook sub-corpus training (75%) and test (25%) sets.\label{r:tt}

               **Sentences**  **Paragraphs**  **Samples**
------------- -------------- --------------- ------------
Training set          40,136           7,314          311
Testing set           13,377           2,436          101
TOTAL                 53,513           9,750          412


\vspace*{-1em}
\begin{tcolorbox}
Predict grade level based on features at all levels.
\end{tcolorbox}

### Results: glmnet Model (2)

\vspace*{-1em}


**Results**   **Sentences**           **Paragraphs**       **Samples**
------------- ----------------------- -------------------- ---------------------
Accuracy :    0.647                   0.665                0.851
95% CI :      (0.639, 0.655)          (0.645, 0.683)       (0.767, 0.914)


<!--
No Information Rate :      0.616                   0.56                 0.614
P-Value [Acc > NIR] :      1.25$\times 10^{-13}$   <2$\times 10^{-16}$  1.53$\times 10^{-7}$
Kappa :                    0.164                   0.35                 0.703
Mcnemar's Test P-Value :   < 2$\times 10^{-16}$    <2$\times 10^{-16}$  0.0117
-->

\small

Variable importance for each model:

-   Sentence: hiragana > kanji > tokens > length ...
-   Paragraph: hiragana > kanji > chunk depth > tokens ...
-   Sample: hiragana > tokens > kanji > chunks ...

\begin{tcolorbox}
Only sample model is effective. Hiragana, kanji and sentence length features predominate.
\end{tcolorbox}

### Readability: Summary

\vspace*{-.5em}

\begin{tcolorbox}[title={Summary}]
\small
\begin{itemize}
\item Most features only effective in predicting readability only at sample level.
\item Sentence length or ratio of kanji in sentence a reasonable heuristic for use in writing assistance systems.
\end{itemize}
\end{tcolorbox}

\vspace*{-.5}

\begin{tcolorbox}[title={Problems}]
\small
\begin{itemize}
\item More research into readability of individual sentences is needed.
\item Future models should target material aimed at L2 Japanese learners instead of Textbook corpus used here.
\end{itemize}
\end{tcolorbox}

# Writing Assistance System (Part III)

## Overview (Ch. 7)

### Overview (Ch. 7)

\centering
\includegraphics[height=.8\textheight]{images/phd-chapter-outline-ch7.pdf}

### System Architecture Overview

\vspace{-2em}
\begin{center}

\includegraphics<1>[height=1.2\textheight]{images/system-architecture-overview-1.pdf}
\includegraphics<2>[height=1.2\textheight]{images/system-architecture-overview-2.pdf}
\includegraphics<3>[height=1.2\textheight]{images/system-architecture-overview-3.pdf}

\end{center}

\note{
Composable system architecture (vs. contextual --- plugin-based).
}

## [Natsume](http://hinoki.ryu.titech.ac.jp/natsume/) (Ch. 8)

### [Natsume](http://hinoki.ryu.titech.ac.jp/natsume/) (Ch. 8)

\centering
\includegraphics[height=.8\textheight]{images/phd-chapter-outline-ch8.pdf}

### [Natsume](http://hinoki.ryu.titech.ac.jp/natsume/)

\centering
\includegraphics[height=.85\textheight]{images/natsume-overview.pdf}

### Collocation Search Interface

\centering
\includegraphics[width=1.01\linewidth,height=.8\textheight]{images/natsume-compare.pdf}


### Genre Comparison Interface

\label{manualcompare}

![Comparing collocations of 'jikken' with 'yaru', 'suru' and 'okonau' across genres](images/natsume-genre-compare.pdf)

\note{
-   writers use the genre comparison feature of Natsume to decide if their word choice is correct for their chosen register
-   problem identified in Natsume evaluation: how to make writers aware of problems in their writing that they do not actively search for?
}

### Example Sentence Interface

\centering
\includegraphics[width=1.01\linewidth,height=.8\textheight]{images/natsume-jikken-examples.pdf}

### [Natsume](http://hinoki.ryu.titech.ac.jp/natsume/) Evaluation

\vspace*{-.2em}

\begin{tcolorbox}[title={Research Question 1}]
\small
Can linguistic resources such as corpora be used to make computer-assisted writing more effective?
\end{tcolorbox}

\vspace*{-.8em}

-   Evaluation 1:
    -   **Informal$\rightarrow$formal sentence rewriting task** with 40 undergraduate participants (January 2011).
    -   Not a writing task $\rightarrow$ seeks to validate the search and genre comparison method in Natsume.
-   Evaluation 2:
    -   **Report writing task** with 20 undergraduate participants (June 2011).
    -   Report writing task $\rightarrow$ seeks to validate Natsume use in a more authentic task.

### Evaluation 1

\vspace*{-.7em}

![](images/experiment-1-design.pdf)

\vspace*{-1.1em}
\small


-   40 Intermediate-Advanced undergraduate L2 Japanese language learners (JLPT 1-2).
-   Two groups (A and B) of similar (pre-test) language proficiency and first language.
-   Two tests (Test 1 and Test 2) of equal difficulty (partially based on JLPT word level).

### Evaluation 1: Results (1)

-   Differences in pre-test, Control and Natsume scores in groups A and B were not significant.
-   Up to 2 points per (NPV) collocation, 1 point for other types of rewriting.

\vspace*{-1em}

![Evaluation scores of Control and Natsume groups.](images/natsume-experiment-2010-boxplot-annotated.pdf)

\vspace*{-.5em}

-   Average scores were higher using Natsume.

### Evaluation 1: Results (2)

\centering
\includegraphics[width=1.01\linewidth,height=.8\textheight]{images/natsume-experiment-2010-lr-figure-en-annotated.pdf}

\vspace*{-.5em}

### Evaluation 1: Summary

-   Overall better performance when using Natsume.
-   Negative linear relationship between language proficiency and improvement in task.

\begin{tcolorbox}[title={Problems}]
\small
5 Intermediate \& Advanced participants achieved better scores on Control.
\end{tcolorbox}

-   High-scoring participants made use of rewriting strategies not covered by Natsume.
    -   More collocation types besides Noun+Particle+Verb are needed to cover wider range of expressions.


### Evaluation 2

\vspace*{-.8em}

![](images/experiment-2-design.pdf)


\vspace*{-1em}


-   Two groups (A and B) of similar (pre-test) language proficiency and first language.
-   Two report themes.
-   Every collocation searched for with Natsume
-   Up to 2 points per (NPV) collocation, 1 point for other types of rewriting.


\note{
-   User profile: Intermediate-Advanced learners of Japanese, Japanese native speakers
-   Enables learners to search for words and word patterns
-   Helps them to make correct use of these patterns according to their writing goal (i.e. paper)
-   Follows the philosophy of data-driven language learning (authentic examples, exploration, etc.)
}

### Evaluation 2: Evaluation Criteria

Register

:   Is the collocation suitable for the academic register?

Semantic.c

:   Is the collocation semantically correct?

Syntax.c

:   Is the collocation grammatically correct?

Semantic

:   Is the usage of the collocation semantically correct with respect to the whole meaning of the sentence?

Syntax

:   Is the usage of the collocation syntactically correct with respect to the syntactic structure of the sentence?


\hline

`.c` $\rightarrow$ Collocation could be correct on its own, but not fit its context.

<!--
5-point Likert scale $\rightarrow$ recoded to 3-point scale
-->

### Evaluation 2: Collocation Evaluation

\vspace{-.2em}
\includegraphics[height=1.4\textheight]{images/natsume-2011-experiment-boxplots-annotated.pdf}


### Evaluation 2: Summary

-   Participants using Natsume's collocation and genre comparison view used better collocations in their reports.

-   Problems:
    -   Participants did not search for words they believed were correct.
    -   More collocation types besides Noun+Particle+Verb/Adverb and Adjective+Noun are needed to cover wider range of expressions.

## [Nutmeg](http://hinoki.ryu.titech.ac.jp/nutmeg/) (Ch. 9)

### [Nutmeg](http://hinoki.ryu.titech.ac.jp/nutmeg/) (Ch. 9)

\centering
\includegraphics[height=.8\textheight]{images/phd-chapter-outline-ch9.pdf}

### [Nutmeg](http://hinoki.ryu.titech.ac.jp/nutmeg/)

Writing assistance system that **identifies errors** in reports and academic prose \parencite{NCYagi2012E}.

-   Detect errors that learners themselves are unaware of.
-   Reduce cognitive burden associated with switching between applications while writing.

\begin{tcolorbox}[title={Research Question 2}]
Is it possible to correct writing style using only corpora?
\end{tcolorbox}

### Nutmeg Interface Overview

\centering
\includegraphics[height=\textheight]{images/nutmeg-interface-summary-mod.pdf}

### [Nutmeg](http://hinoki.ryu.titech.ac.jp/nutmeg/) Error Feedback

\vspace{-.5em}
\small

-   Underlines errors + provides feedback on mouse hover.
-   When possible, provides an explanation of why the system thinks there is an error.

\vspace*{-.8em}
\centering
\includegraphics[height=.55\textheight]{images/nutmeg-writing-interface.pdf}

### Register Identification Method (1)


\centering
\includegraphics[height=.2\textheight]{images/natsume-genre-compare.pdf}

-   Formalization of manual comparison method in Natsume (see Slide \ref{manualcompare}).
-   Limited to identifying collocation misuse in paper and report writing, by comparing formal/academic corpora with informal/spoken corpora:
    -    **STJC + White papers** $\rightarrow$ proxy corpora for paper and report writing ($C_+$).
    -    **Diet minutes + Yahoo! Q&A + Yahoo! Blogs** $\rightarrow$ proxy for informal/spoken writing ($C_-)$.

### Register Identification Method (2)

\footnotesize

1.  Perform the $\chi^2$ test for variance on the relative frequency $f$ of a word or collocation on all corpora $C_0, C_1, \cdots, C_N$, with average frequency across all corpora denoted by $\bar{f_K}$

    \begin{equation}
    \Delta f(k) =
    \begin{cases}
    f(k) - \bar{f_K}, &\text{if } \frac{(f(k) - \bar{f_K})^2}{\bar{f_K}} > \chi^2(\text{df}=N-1; p=0.05)\\
                   0, &\text{otherwise}
    \end{cases}
    ; \forall k \in 0, \cdots, N
    \end{equation}
2.  Assign corpora to the positive ($C_+$) and negative ($C_-$) groups, compare their sum, and compute the score for any chosen word $s$

    \begin{equation}
    s =
    \begin{cases}
     1, & \text{if } (\sum_{j \in C_+}\Delta f(j) \ge 0) \wedge (\sum_{j \in C_-}\Delta f(j) < 0) \rightarrow \text{correct usage}\\
    -1, & \text{if } (\sum_{j \in C_+}\Delta f(j) \le 0) \wedge (\sum_{j \in C_-}\Delta f(j) > 0) \rightarrow \text{incorrect usage}\\
     0, & \text{if neither is statistically significant} \rightarrow \text{no result}
    \end{cases}
    \end{equation}


### Register Identification Method (3)

\vspace*{-.5em}

Use learner mistakes and their corrections from the Natane Learner corpus to measure method accuracy.

Table: Results from word-level experiment (corrections classified as register-related in Natane).

                 Uncorrected          Corrected
------------- -------------- ------ ----------- ------
Identified                44  (79%)          10  (15%)
Unidentified              12  (21%)          57  (85%)
TOTAL                     56                 67

\begin{tcolorbox}
\small
While it is possible to detect probable mistakes (79\%), corrections made by annotators were harder to detect as correct (only 15\%).
\end{tcolorbox}


A similar experiment performed on collocations is available in [@NCYagi2012E].

<!-- Actually, probably @ICJLEYagi2012 FIXME -->


<!--
### Correction Based on Contextual Model

#### Proposed Method (1): Employed in Nutmeg

-   Formalization of manual comparison method in Natsume
-   Limited to correcting paper and report writing, by comparing formal/academic corpora with informal/spoken corpora
    -    STJC + White papers $\rightarrow$ proxy corpora for paper and report writing
    -    Diet minutes + Yahoo! Q&A + Yahoo! Blogs $\rightarrow$ proxy for informal/spoken writing
-->

<!--
### Correction Based on the Contextual Model

#### Proposed Method (2): Based on Model of Context

\begin{tcolorbox}
Use the three models of context (register, topic and readability) to provide corrections based on writing context.
\end{tcolorbox}

-   distances between corpora used to weight the occurrence of some word or collocation depending on the writing context


\note{
Problems with the previous model:

-   the choice of positive and negative corpora are "ad-hoc", based on researcher's perceived differences between corpora

Proposed method:

-   use the three models to measure the distances between corpora
    1.   register model (TODO)
    2.   topic model
    3.   readability model
}
-->

## Integrated System (Ch. 10)

### Integrated System (Ch. 10)

\centering
\includegraphics[height=.8\textheight]{images/phd-chapter-outline-ch10.pdf}

### Expansion of Collocation Patterns

When conducting Evaluations 1 and 2, Natsume had access to 2.3 million different NPV collocations (8.7 million total) and three different collocation patterns: NPV, NPAdj and AdjN.

\small

Table: Current number of 3-gram relations (top 6).\label{n3}

**Relation**                 **Count**  **Unique**
------------------------- ------------ -----------
noun_particle_verb          47,820,467  25,997,330
noun_particle_noun          29,175,328  20,810,250
verb_noun_particle           9,946,758   5,862,717
noun_noun_particle           6,671,190   4,887,841
verb_particle_verb           4,034,753   2,266,622
adverb_particle_verb         3,543,971   1,232,097
\cdots                          \cdots      \cdots
TOTAL                      125,002,194  74,422,671


### Integrated System

Online browser-based editor integrating the three models of context.

1.  Decisions based on knowledge of writer's proficiency level, chosen writing topic and target audience.
2.  Identify and provide corrections for word and collocation usage that are specific to the writer's target register, topic and readability.
3.  Show documents related to the writer's text with respect to register, topic and readability.

<!--

### Model Integration

\begin{tcolorbox}[title={Register}]
\begin{itemize}
  \item Identify word and collocation register misuse $\rightarrow$ automatic register correction.
  \item Classify register of user text $\rightarrow$ sentence and text-level register classification.
\end{itemize}
\end{tcolorbox}

\begin{tcolorbox}[title={Topic}]
\begin{itemize}
  \item  $\rightarrow$
  \item Classify topic of user text $\rightarrow$ sentence and text-level .
\end{itemize}
\end{tcolorbox}

\begin{tcolorbox}[title={Readability}]
\being{itemize}
  \item identify word level $\rightarrow$
  \item identify sentences with low readability, provide readability report for whole text $\rightarrow$
\end{itemize}
\end{tcolorbox}
-->

<!--

Two levels of assistance:

1.  Word and collocation level
    -   Register: identify register misuse in words and collocations
    -   Topic: identify words and collocations with similar topics
    -   Readability: identify word level

2.  Text level
    -   Register: identify closest registers to input text
    -   Topic: identify topics similar to input text
    -   Readability: identify sentences with low readability, provide readability report for whole text

-->

\note{

Features:

-   all aspects of the system act on the knowledge of the writer's proficiency level, chosen writing topic and target audience
-   identify and provide corrections for word and collocation usage that are specific to the writer's target *register*, *topic* and *readability* (direct feedback)
-   show the writer how close the writing is to multiple genres, with respect to register, topic and readability (indirect feedback)

-   what features should we allow the user to set: i.e. language proficiency, genre knowledge, reader language prof+genre knowledge
}


<!--
### Evaluation

#### Evaluation (1): Data

-   Classification performance of models
-   ['Natane'](http://hinoki.ryu.titech.ac.jp/natane/) Japanese learners corpus: contains around 200 corrected reports and essays by Japanese learners
    -   Measure the precision and recall of correction features

\note{
Natane (cf. \parencite{dale2012framework}, ["Helping Our Own" project](http://clt.mq.edu.au/research/projects/hoo/)).
-   One "problem" with Natane is the inclusion of a lot of register annotations/corrections that might not appear in other more general essay-like learner corpora, but as this is the point of my research, this is a given and should be said up-front
}

#### Evaluation (2): Experiment

-   Japanese learners and native Japanese speakers

\note{

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

}
-->

# Conclusion (Part IV)

## Conclusion (Ch. 11)

### Conclusion (Ch. 11)

\centering
\includegraphics[height=.8\textheight]{images/phd-chapter-outline-ch11.pdf}

### Conclusion

\begin{tcolorbox}
\begin{itemize}
\item Developed three models of writing context: register, topic and readability.
\item Collaborated in the construction of two writing assistance systems.
\item Evaluated Natsume and the register identification method in Nutmeg.
\item Increased collocation count and variety.
\item Proposed integration of models with systems.
\end{itemize}
\end{tcolorbox}

<!--
1.  Depends only on genre-labeled language data
    -   Writing contexts other than report writing can be added as long as there is sufficient language data
2.  Possible to increase learner awareness towards differences in language
    -   Close the experience gap between second language and native writers, non-experts and experts
-->

### Future Work

-   Integration of models into system.
    -   Evaluation of model error prediction performance using the Natane Learner corpus.
-   New interface needed for increase in collocation types.
-   Evaluation of new system features.
    -   L2 Japanese learners and native Japanese speakers (academic writing).
-   Integration of system use in academic writing curricula.

\note{
-   compared to existing systems that do not take into account the writer's context, \ldots


作文支援システム構築のため、言語資源を用いて、自然言語処理で可能な部分を実現させること

教育（学習）的視点からは、レジスターの理論的フレームを利用して、学習者（論文などを書く必要のある留学生）に　レジスターの概念を意識化させることをある程度実現したということだと思います。

理論的には、　教育工学ではdata　driven　learning　、言語学では機能文法（Halliday）,Topic理論、言語処理では、統計手法（Biber を含む）機械学習の考え方... このような理論的な枠組みで新しい考えがどう埋めれたかをアピールすることが最も重要です。

つまり、今までなかったもの、できなかったことをどのようにして、新しい手法を確立し、何を可能にしたかということです。

}

<!--
# References

### References

\footnotesize

-   James E Hoard, Richard Wojcik, and Katherina Holzhauser. “An automated grammar and style checker for writers of Simplified English”. In: Computers and Writing: State of the Art (1992), pp. 278–296.
-   Tomoya Mizumoto and Mamoru Komachi. “Robust NLP for Real-world Data: 3. Why is Japanese so Hard to Learn?—A Preliminary Investigation on Realistic Japanese Learners’ Corpus and Application of Natural Language Processing to Japanese Language Learning and Education—”. In: IPSJ Magazine 53.3 (Feb. 2012), pp. 217–223.
-   Wilburt Schramm. “The Process and Effects of Mass Communication”. In: (1955), pp. 3–10, 13, 17.

-->
