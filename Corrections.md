%
% Bor Hodošček
% \today

# Correction (Diff)

## TODO

### Experiment 1

![Cross-over balanced repeated-measures design.](images/experiment-1-design.pdf)

Table: Summary of available data (K = number of collocations per participant).

Data         Type              Within/Between  Type of variable     Possible values      Comment/Restraint
------------ ----------------- --------------- -------------------- -------------------- -------------------------------------------
Lang. prof.  nuisance          between         interval             0-50                 block, balanced, fixed effect
L1           nuisance          between         categorical          Chinese, Korean, ... block, balanced, fixed effect
nationality  nuisance          between         categorical          Chinese, Korean, ... block, balanced, fixed effect
major        covariate         between         categorical          ...                  random effect
sex          covariate         between         categorical          male, female         random effect
age          covariate         between         numerical            0-                   random effect
study.months covariate         between         numerical            0-
JLPT         covariate         between         ordered categorical  1, 2, 3, 4           NA
EJU          covariate         between         interval             0-450                NA, Japanese test score only
textbooks    covariate         between         categorical (list)   ...                  NA
group        independent       between         categorical          A, B                 block, balanced, fixed effect
test         independent       within          categorical          1, 2                 block, balanced, fixed effect
condition    independent       within          categorical          control, treatment   repeated-measure, main effect, fixed effect
score        dependent         between+within  numerical            0-23                 (collocation + other score)

-   Analysis
    -   FIXME add pre-test language proficiency scores!
    -   Scatterplot first. Differences between groups and measures.
    -   Repeated-measures (condition: control, treatment) AOV/GLM on score.
        -   Two-way (test, group) mixed-model repeated-measures (condition: control, treatment) analysis of covariance.
            -   lmer(Score ~ Condition * Test + (1 | Group/Subjects), data = m)
            -   What is the correct Error formula?
            -   Try 2 GLMs, by splitting on group.
            -   Test is nested in Group.
        -   Check normality assumptions.
        -   (Low priority) Covariate NAs: try `mice()` or other imputation methods
            -   MARS, MAR, or ?

<!--
> A randomized block design arranges experimental units in groups (blocks) that are similar to one another.
> Typically, a blocking factor is a source of variability that is not of primary interest to the experimenter.
> An example of a blocking factor might be the sex of a patient; by blocking on sex, this source of variability is controlled for, thus leading to greater accuracy.
> A nuisance factor is used as a blocking factor if every level of the primary factor occurs the same number of times with each level of the nuisance factor. The analysis of the experiment will focus on the effect of varying levels of the primary factor within each block of the experiment.
>
> The nuisance factors here are: theme/test, L1, Ext. proficiency score.
-->

<!--
1.  Multiple linear regression with control and treatment scores as dependent, and all others as independent variables.
    -   Also COANOVA (check [this](http://www.statmethods.net/stats/anovaAssumptions.html) and [this](http://little-book-of-r-for-multivariate-analysis.readthedocs.org/en/latest/src/multivariateanalysis.html))
    -   Used to predict numerical variables
2.  If that does not give strong results, you can try discriminant analysis (using [arcsine angular transformation method](http://rfd.uoregon.edu/files/rfd/StatisticalResources/arcsin.txt))
    -   (L)DA should be used to predict categorical variables
-->

\newpage

### Experiment 2

![Cross-over balanced repeated-measures design.](images/experiment-2-design.pdf)

Table: Summary of available data (K = number of collocations per participant).

Data         Type              Within/Between  Type of variable     Possible values      Comment/Restraint
------------ ----------------- --------------- -------------------- -------------------- -----------------------------
Lang. prof.  nuisance          between         interval             0-50                 block, balanced
L1           nuisance          between         categorical          Chinese, Korean, ... block, balanced
sex?         covariate?        between         categorical          male, female         block, balanced??
group        independent       between         categorical          A, B                 block, balanced
theme        independent       within          categorical          1, 2                 block, balanced
condition    independent       within          categorical          control, treatment   repeated-measure, main effect
time         dependent         between+within  interval             30-60 min.
search freq. dependent         between         numerical            0-                   condition==treatment
tokens       dependent         between+within  numerical            0-
register     dependent         between+within  ordinal (x 3 x K)    1-5
syntax       dependent         between+within  ordinal (x 3 x K)    1-5
syntax.c     dependent         between+within  ordinal (x 3 x K)    1-5
semantic     dependent         between+within  ordinal (x 3 x K)    1-5
semantic.c   dependent         between+within  ordinal (x 3 x K)    1-5
survey.Q1    other             between+within  ordinal              1-5
survey.Q2    other             between+within  ordinal              1-5
...          ...               ...             ...                  ...
survey.QN    other             between+within  ordinal              1-5


<!-- nuisance variable ~= confounding factor -->

-   Analysis
    -   Check normality assumptions.
    -   (Probably impossible) Multivariate (scores ($\times$ 5), time, tokens) two-way (theme, group) mixed-model repeated-measures (condition: control, treatment) analysis of covariance.
        -   Within-subjects makes more sense for measuring the effect of the Condition and theme, while Between-subjects makes more sense for measuring the effect of the nuisance and blocking variables.
        -   If we treat scores as ordered factors (Likert scale), then we need to use a logistic GLM.
    -   Differences in means between within- and between-subjects groups.

        For this part, we want to check to validity of the experiment with respect to the nuisance variables (language proficiency, L1), the block variable (theme), as well as the repeated measure (register, ... ← Probably not possible)
        -   Check with TukeyHSD.
    -   Sum differences in means between conditions.

        For this part, we want to aggregate all Likert scores, grouping by repeated measure (condition: control, treatment)
        -   Inter-annotator agreement used to find acceptable point scale.
        -   Crombach's alpha (for both point scales if recording is done).
        -   Analysis
            -   How to group/accumulate these scores?
                -   Ordered factor.
            -   $t$-test.
            -   $\chi^2$ test on contingency table of summed ordinal Likert data.
        -   How to account for order effects?
    -   Survey data box-plots.
        -   (Low priority) FA.

-   Summary
    -   Groups not sig. different in lang. prof., essay length or time.
    -   Theme 2 takes around 6 minutes longer than Theme 1 (p < 0.05) and tendency to have more types per essay.
        -   Check data! theme = condition ?????
    -   Condition does not effect time, tokens, or types significantly.

Table: Paired $t$-tests. FIXME replace with multiple comparison.

t-test on  time     lang. prof.  tokens  types
---------- -------- ------------ ------- ---------
group      n.s.     n.s.         n.s.    n.s.
theme      -2.56*   N/A          n.s.    -1.73.
condition  n.s.     N/A          n.s.    n.s.

-   Data #1
    -   Within+Between-subject dependent variable (scale): time (minutes) (A|B X 1|2) ()
    -   Between-subject dependent variable (scale): treatment Natsume search frequency (A|B)
    -   Within+Between-subject dependent variable (scale): essay length, types, tokens, ... (A|B X 1|2) (Within-subjects makes more sense for measuring the effect of the Condition, while Between-subjects makes more sense for measuring the effect of essay theme)
    -   Within+Between-subject dependent variable (scale): collocation evaluation scores (NAs exist) (A|B X 1|2)

-   Data #2 (grouped data): group A + B
    -   control collocation evaluation scores
        (3 annotators $\times$ total # of collocations for groups A+B $\times$ 5 evaluation items (5-point scale))
    -   treatment collocation evaluation scores
        (3 annotators $\times$ total # of collocations for groups A+B $\times$ 5 evaluation items (5-point scale))

-   Data #3: Survey data
    -   Crombach's alpha
    -   Factor analysis/C4.5/cluster analysis?
-   If possible, do in first analysis (or at least with Data #1)

Formula: y ~ covariates + main effects + two-way interactions + three-way interactions + ...
General formula: c(register, syntax, syntax.c, semantic, semantic.c, time, tokens, search freq.) ~ condition * theme * group + Error(id/(condition * theme))
Also: When the research design isn't orthogonal (that is, when the factors and/or covariates are correlated), be careful when specifying the order of effects.


> aov(c(register, syntax, syntax.c, semantic, semantic.c, time, tokens) ~ )
>
> linear mixed model:
>
> nlme(c(register, syntax, syntax.c, semantic, semantic.c, time, tokens) ~ )


\newpage

#### Analysis

-   [✓] Inter-annotator agreement
-   Check if ANOVA normality assumptions hold
-   sABデザイン(２要因参加者内計画)
    -   Repeated measures ANOVA?
    -   Linear mixed model?
-   Does balanced design require all nuisance variables to be balanced, or just subject numbers to be the same?
-   Small points:
    -   'order' effects: does the order in which treatments are administered affect the outcome?
        -   practice, boredom, and fatigue
    -   'carry-over' between treatments: confounds the estimates of the treatment effects
        -   Writing one essay after another might be easier as the writer has a mental model of the structure and argumentation of the previous essay already formed.
            The effect of this would be great if the topics given were similar, but they were not.
    -   'learning' effect: This is important where you have controls who are naive to the intended therapy. In such a case e.g. you cannot make a group (typically the group which learned the skill first) unlearn a skill such as yoga and then act as a control in the second phase of the study.

-   need to answer the question: What kind of variability in the experimental design do we expect, and how does the design minimize them?
    -   When choosing between Completely randomized design or randomized block design or a cross-over design?
        -   Is the natural variability within a subject likely to be small relative to the natural variability across subjects?
        -   Are there likely to be carry-over effects?
        -   Are there likely to be ``drop-outs''?
        -   Is a cross-over design feasible?

\newpage

## Questions

①本論文2つのRQsを解決したか？

②名義尺度と間隔尺度が混在したときの分析方法が間違ったのではないか？

③コーパス自体の性質を考えるべきではない

④サンプルの母集団問題

⑤モデルの問題（誤解されやすい）

⑥レジスターを深める方法を考えるべきではないか。

⑦ReaderとWriterに分けて検討した方がよいのではないか。

⑧S42（？）Pre-test：A・B両群には差がなかったのに、統制群と条件群には有意差が見られたのと混同したのではないか。

⑨今後本研究の汎用性（共起のつながりの適用範囲、等）


上記の問題ですが、簡単にクリアできるものもあれば、もっと根本的に考えてから修正するものもあるかと思います。例えば①RQはそのままにして、研究ごとに仮説を立てて検討するのはよくあるパターンですので、分けてみてもよいのかもしれません。②はクリアしやすく、⑧は同質性を保つため、事前テスト両群に差がないことが確認され、そのうち、条件群と統制群には差が見られたのは、立派な結果です。⑦はそもそも本研究の対象で、その必要性を明確に説明すれば問題ないと思いまして、⑨は本研究の適応範囲を示せば済む話しだと思われます。③、④、⑤、⑥は室田先生や仁科先生にご相談のうえ、大いに修正が必要なところだと思われます。


次は私がプレゼンを聞いた時の感想です。

①定義を明確にする箇所があります。例えば、S36の「High frequency」ですが、何をもってそう言えるのかどこにも触れていませんので、一言でもよいので、基準を言及する必要があると思いました。

②2つのEvaluationですが、学習者の属性とかまったく触れなくて、結果（負の相関）から結論付けられるのは弱いのではないかと思いました。日本語学習は日本語能力だけでなく、出身地・日本語学習歴・滞日歴・男女差、等の要因が絡んでますので、そういう属性を1つの表とかにまとめて、日本語レベルや男女差、学習歴、滞日歴によって差があるかどうか、そして出身地によって違いがあるかどうか、あるとしたらどんなものなのか、を検討すべきだと思いました。
もし②を詳しく分析するのではれば、学習歴・滞日歴・男女差、などは簡単に分析できると思いますが、出身地の場合はおそらく「角変換」にしたうえ、ANOVAもしくはt検定を行って、はじめて結果が言えるのではないかと思います。

③ほかには、Chapter 5と6に、BCCWJ Topic相関が見られましたが（S28、30）、果たしてそれ以外のものがないのか、言えないのではないかと思いました。他に影響を及ぼす要因があるかもしれませんし、相関になったどちらが原因という可能性もありえますので。


### (Prof. Nakayama)

1.  ２つのRQは解けたか？
2.  どういったコーパスが効果をもたらしている？そのコーパスのどのような性質が関わるか？
    -   make it more clear that we are interested in differences: i.e. we can get more information from having more variation.
3.  学習者にどのような指示をしたことを明記すること
4.  44枚目のスライドの修正・解明（名義尺度と回帰など）：名義尺度と間隔尺度が混在したときの分析方法が間違ったのではないか？

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
            -   Just need to be more clear here and fix p. 59/60 in the paper ('scores' can refer to Natsume and Control, but in this case really refer to pre-test scores). The ref and label need to be fixed to refer to the right results.

## Answer

1.  Resampling

    Cross-validation vs. permutation tests.
    75:25 train/test data split (I should have used held-out data).

### (Assoc. Prof. Yamamoto)

1.  Schrammのfield of experienceを使っているが、intersectionが大きければ大きいほど、理解があると書いてある。その２つのフィールドが時代を超越してあったり、または専門が違っていたり、またはそれぞれの人間の？？が違っていたりすることで理解が得られないということ。field of experienceの中を深めてその中のsignalについて、レジスターに関する要素が、sharedすればするほど理解度が大きい、そして同じようにトピックがある。そのschemaについて、レジスター的なFOEがある、そしてトピックとしてみたFOEがある、が、signalそのものは変わらない？レジスター、トピックなどはFOEの一つの見方なのでしょうか（はい。）。
    -   the lines from register/topic/... shared FOE look like they point to the signal, while they should only point to the highlighted area.

2.  単なるシグナルを教えるだけでは、どうしようもないレベルで、レジスターのようなもののed areaを広げていくとか、トピックに関するshared areaを広げていくことを組み合わせるものとして、この研究が始まったのかな。その研究の一環として一つはレジスターを深めたという考え方でよろしいでしょうか？WriterとReaderのレジスターを分離して考えるというアプローチはありませんでしたか？

### (Prof. Nohara)

1.  Generalityに関する問題で、コロケーションの結びつき（まとまり、つながり）の強さがレジスターによって異なるとして、ほかのレジスターにも適応できるか、その展望について説明してください。
    -   The association strength of collocations per register is probably a function (or at least affected by it) of the inter- and intra- variability in registers and topics per corpus. Possible ways to see differences here is to compare collocation measure scores and average collocates per word by corpus (ltree) and see how much of an effect this could have. Also need to find some research to even back Prof. Nohara's statement, though it seems reasonable. We should watch out for similar text length vocabulary changes too (maybe Yule's k?).
    -   The generality is limited by the need for a target corpus that aligns with the writer's target area (in register, topic and readability).
        -   Pedagosko predstavljen problem: zato imamo en korpus.

------

Operacijsko definirani modeli realnosti.
Kaj je pa realnost?
