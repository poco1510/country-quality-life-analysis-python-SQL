# Country's Quality of life - analysis

This project ingests country and economic datasets into a SQLite database, performs exploratory data analysis, and visualizes key insights such as GDP, education expenditure, and trade/export metrics and compares these economic factor and their role in improving country's "Quality of life".

---
## Table of contents
- <a href="#overview">Overview</a>
- <a href="#dataset">Dataset</a>
- <a href="#tools-technique">Tools&Technique</a>
- <a href="project-structure">Project Structure</a>
- <a href="country-Qualitylife-analysis">Quality life in countries</a>
- <a href="key_findings">Key Findings</a>
- <a href="how-to-run-this-project">How to run this project</a>
- <a href="author-contact">Author & Contacts</a>
---
<h2><a class="anchor" id="overview"></a>Overview</h2>

This project evaluates the dependencies between "Quality of life" vs Economic factors such as exports, education, purchasing power index . I also found the relationship betwen govt. type and the quality of life and deduce some useful insights and plotted those insight using interactive plots like regression pplot , barplot,line plot.

---
<h2><a class="anchor" id="dataset"></a>Dataset</h2>

- CSV ingestion from the `data/` folder into `inventory.db`
- SQL-based exploration of country-level indicators
- Data profiling and ETL generation
- Plot creation for descriptive analysis and stored in `images/`.

---
<h2><a class="anchor" id="tools-technique"></a>Tools&Technique</h2>
- SQL(common table expression , joins, Filtering)
- Python(Pandas,Pathlib,Matplotlib,Seaborn)
- GitHub

---

<h2><a class="anchor" id="project-structure"></a>Project Structure</h2>

```
country-quality life-analysis/
│
├── README.md
├──.gitignore
├── Quality life report.pdf
│   
├──Scripts/
│   ├──ingestion.py
│   └──ETL pipeline.py
│
├──notebooks/
   └──country-analysis.ipynb
```
---
<h2><a class="anchor" id="country-Qualitylife-analysis"></a>Quality life in countries</h2>

**relation between quality life vs Export,Purchasing power and Education:**
-with export-no impact, as slope remains parallel to x axis
-with purchasing power-hiegher impact,as slope increases.
-with Eduaction-also high impact.

---
<h2><a class="anchor" id="key_findings"></a>Key Findings</h2>

1.  Quality life majorly depends on public purchasing power.
2.  Education plays a vital role in devloping standard of living
3.  The adopted govt type can ensure public safety but can  guarantee Quality of life

---
<h2><a class="anchor" id="how-to-run-this-project"></a>How to run this project</h2>

1.  Clone the repository:
```bash
git clone https://github.com/yourusername/country-quality-life-analysis.git
```
2.  load csvs and ingest into database:
```bash
python scripts/ingestion.py
```
3.  create ETL pipeline:
```bash
python scripts/ETL.py
```
4. open and run notebooks:
  - `notebooks/country-analysis.ipynb`

---
<h2><a class="anchor" id="author-contact"></a>Author & Contacts</h2>

**Jitendr pandey**
Data Analyst
    🔗[linkedIn](https://www.linkedin.com/in/jitendr-pandey-35a5a8419/)
    📩Email: jiti4385@gmail.
---    