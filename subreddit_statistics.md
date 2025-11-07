# Reddit Subreddit Analysis Statistics

## Scraping Metadata

### Total Posts Scraped: 249 posts

| Subreddit | Posts Scraped | Percentage |
|-----------|--------------|------------|
| r/InternationalStudents | 49 | 19.7% |
| r/college | 61 | 24.5% |
| r/StudentLoans | 50 | 20.1% |
| r/financialaid | 50 | 20.1% |
| r/Harvard | 50 | 20.1% |

**Output Directory:** `/Users/lucianadiasdemacedo/Downloads/corpus_expansion/reddit_students/`

---

## r/InternationalStudents Emotion Analysis

### Posts Analyzed: 49

### Emotion Distribution

| Emotion | Count | Percentage |
|---------|-------|------------|
| Hope | 14 | 24.1% |
| Sadness | 8 | 13.8% |
| Joy | 7 | 12.1% |
| Fear | 7 | 12.1% |
| Relief | 6 | 10.3% |
| Despair | 5 | 8.6% |
| Anger | 5 | 8.6% |
| Anxiety | 3 | 5.2% |
| Confusion | 3 | 5.2% |
| **TOTAL** | **58** | **100%** |

### Top 20 Entities

| Entity | Mentions | Category |
|--------|----------|----------|
| US | 173 | Location |
| visa | 137 | Immigration |
| Canada | 87 | Location |
| Indian | 78 | Nationality |
| Indians | 76 | Nationality |
| OPT | 72 | Immigration |
| India | 67 | Location |
| F1 | 52 | Immigration |
| immigration | 51 | Immigration |
| America | 49 | Location |
| American | 47 | Nationality |
| H1B | 43 | Immigration |
| Americans | 41 | Nationality |
| China | 38 | Location |
| U.S. | 37 | Location |
| Chinese | 35 | Nationality |
| Trump | 32 | Person |
| USA | 32 | Location |
| tuition | 22 | Education |
| college | 22 | Education |

### Key Emotion-Entity Connections

#### HOPE (14 occurrences)
- US (63×)
- visa (43×)
- Canada (28×)
- immigration (25×)
- OPT (22×)

#### ANXIETY (3 occurrences)
- OPT (18×)
- US (15×)
- Canada (9×)
- college (9×)
- visa (5×)

#### FEAR (7 occurrences)
- OPT (26×)
- US (23×)
- America (18×)
- visa (13×)
- U.S. (11×)

#### SADNESS (8 occurrences)
- Indians (36×)
- Indian (30×)
- US (22×)
- Canada (20×)
- visa (19×)

#### DESPAIR (5 occurrences)
- US (16×)
- Canada (15×)
- immigration (12×)
- visa (9×)
- American (9×)

#### RELIEF (6 occurrences)
- Canada (15×)
- visa (13×)
- US (11×)
- America (8×)
- Indians (8×)

---

## r/college Emotion Analysis

### Posts Analyzed: 61

### Emotion Distribution

| Emotion | Count | Percentage |
|---------|-------|------------|
| Anxiety | 24 | 22.4% |
| Hope | 23 | 21.5% |
| Joy | 14 | 13.1% |
| Relief | 12 | 11.2% |
| Anger | 12 | 11.2% |
| Fear | 10 | 9.3% |
| Sadness | 10 | 9.3% |
| Confusion | 7 | 6.5% |
| Despair | 5 | 4.7% |
| **TOTAL** | **107** | **100%** |

### Top 20 Entities

| Entity | Mentions | Category |
|--------|----------|----------|
| college | 304 | Education |
| professor | 166 | Education |
| university | 66 | Education |
| campus | 46 | Education |
| major | 45 | Education |
| GPA | 39 | Education |
| RA | 34 | Education |
| College | 28 | Education |
| tuition | 26 | Education |
| dorm | 26 | Education |
| financial aid | 26 | Education |
| AI | 25 | Technology |
| US | 19 | Location |
| FAFSA | 18 | Education |
| America | 13 | Location |
| Trump | 12 | Person |
| CC | 12 | Education |
| debt | 12 | Finance |
| University | 11 | Education |
| Dean | 10 | Education |

### Key Emotion-Entity Connections

#### ANXIETY (24 occurrences)
- college (157×)
- professor (74×)
- university (35×)
- campus (32×)
- RA (27×)

#### HOPE (23 occurrences)
- college (165×)
- professor (59×)
- major (32×)
- university (27×)
- dorm (16×)

#### FEAR (10 occurrences)
- college (85×)
- professor (21×)
- campus (11×)
- RA (10×)
- College (9×)

#### SADNESS (10 occurrences)
- college (57×)
- professor (27×)
- campus (21×)
- university (12×)
- dorm (11×)

#### DESPAIR (5 occurrences)
- college (20×)
- professor (19×)
- GPA (12×)
- financial aid (10×)
- university (9×)

#### RELIEF (12 occurrences)
- college (111×)
- professor (31×)
- major (18×)
- university (16×)
- tuition (12×)

#### JOY (14 occurrences)
- college (76×)
- professor (54×)
- major (17×)
- AI (16×)
- campus (15×)

#### ANGER (12 occurrences)
- college (61×)
- professor (47×)
- RA (18×)
- AI (18×)
- university (18×)

---

## Key Insights - r/InternationalStudents

### Interesting Emotion-Entity Connections:

**HOPE** → US (63×), visa (43×), Canada (28×), immigration (25×)

**ANXIETY** → OPT (18×), US (15×), Canada (9×), college (9×)

**FEAR** → OPT (26×), US (23×), America (18×), visa (13×)

**SADNESS** → Indians (36×), Indian (30×), US (22×), Canada (20×)

**DESPAIR** → US (16×), Canada (15×), immigration (12×), visa (9×)

**RELIEF** → Canada (15×), visa (13×), US (11×), America (8×)

### Notable differences from r/college:

- **Immigration dominates:** visa (137 mentions), OPT (72), H1B (43), deportation (8)
- **Nationality focus:** Indian/Indians (154 combined), Chinese (35), Canada-focused migration
- **Geographic spread:** 50+ countries mentioned vs US-centric in r/college
- **Hope is tied to immigration:** Top hope connections are US, visa, Canada, immigration
- **Fear/Anxiety center on work authorization:** OPT appears in top fear (26×) and anxiety (18×) connections
- **Sadness strongly linked to ethnic identity:** Indians/Indian as top sadness entities
- **Relief comes from alternatives:** Canada (15×) represents alternative pathway/relief
- **Less academic stress:** GPA barely mentioned, professors not a major concern
- **Political figures prominent:** Trump (32 mentions) - 2.7× more than r/college
- **Despair is systemic:** Connected to immigration system, not individual performance

---

## Key Insights - r/college

### Interesting Emotion-Entity Connections:

**ANXIETY** → college (157×), professor (74×), university (35×), campus (32×)

**HOPE** → college (165×), professor (59×), major (32×)

**DESPAIR** → college (20×), professor (19×), GPA (12×), financial aid (10×)

**FEAR** → college (85×), professor (21×), campus (11×), RA (10×)

**RELIEF** → college (111×), professor (31×), major (18×), university (16×)

**JOY** → college (76×), professor (54×), major (17×), AI (16×)

### Notable differences from r/InternationalStudents:

- **Much higher focus on professors and campus life:** professor (166 mentions vs 0 in international)
- **GPA is a major concern:** 39 mentions (critical for despair connections)
- **Less focus on visa/immigration:** only 19 US mentions vs 173 in international students
- **Strong connection between despair and GPA/financial aid:** Academic performance drives despair
- **Residential life matters:** RA (34), dorm (26), campus (46) - daily college experience
- **Financial stress is domestic:** FAFSA (18), financial aid (26), debt (12), student loans
- **AI emerges as topic:** 25 mentions, connected to joy (16×)
- **Anxiety is highest emotion:** 24 occurrences (22.4%) vs only 3 (5.2%) for international students
- **Professors are everywhere:** Connected to every major emotion
- **Hope and anxiety both peak with same entities:** college & professor appear in both

---

## Comparative Analysis

### Emotion Comparison

| Emotion | r/InternationalStudents | r/college | Difference |
|---------|------------------------|-----------|------------|
| Anxiety | 3 (5.2%) | 24 (22.4%) | +17.2% |
| Hope | 14 (24.1%) | 23 (21.5%) | -2.6% |
| Joy | 7 (12.1%) | 14 (13.1%) | +1.0% |
| Fear | 7 (12.1%) | 10 (9.3%) | -2.8% |
| Sadness | 8 (13.8%) | 10 (9.3%) | -4.5% |
| Anger | 5 (8.6%) | 12 (11.2%) | +2.6% |
| Relief | 6 (10.3%) | 12 (11.2%) | +0.9% |
| Despair | 5 (8.6%) | 5 (4.7%) | -3.9% |
| Confusion | 3 (5.2%) | 7 (6.5%) | +1.3% |

### Key Insights

**r/InternationalStudents:**
- **Dominant theme:** Immigration and visa concerns
- **Top emotion:** Hope (24.1%)
- **Primary focus:** US, visa, Canada, OPT, immigration status
- **Strong sadness connection:** Indian/Indians nationality + visa/immigration issues
- **Fear/Anxiety:** Heavily linked to OPT and visa status

**r/college:**
- **Dominant theme:** Academic life and campus experience
- **Top emotion:** Anxiety (22.4%)
- **Primary focus:** professor, college, campus, GPA, financial aid
- **Despair connection:** GPA and financial aid issues
- **Anxiety peaks:** Related to professors, RA (Resident Advisors), campus life

**Notable Contrasts:**
1. **Anxiety:** r/college shows 4.3× more anxiety (24 vs 3 occurrences)
2. **Immigration focus:** r/InternationalStudents has 137 visa mentions vs 2 in r/college
3. **Academic stress:** GPA appears 39× in r/college vs rarely in r/InternationalStudents
4. **Financial concerns:** Both show high financial stress but different sources (tuition/FAFSA vs visa/deportation)
5. **Geographic diversity:** r/InternationalStudents mentions 50+ countries; r/college is US-centric

---

## Files Generated

- **International Students Graph:** `graph_internationalstudents_emotions.html`
- **College Graph:** `graph_college_emotions.html`
- **International Students Data:** `internationalstudents_analysis.json`
- **College Data:** `college_analysis.json`
- **Individual Annotated Posts:** `/Users/lucianadiasdemacedo/Downloads/corpus_expansion/annotated_posts/`
