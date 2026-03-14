# Clinical AI Pipeline Evaluation Report

Overview

This project evaluates the reliability of a clinical AI pipeline that extracts structured medical entities from OCR-processed medical charts.
The dataset contains 30 clinical charts, each with extracted entity data and OCR text.

The goal is to identify weaknesses in the AI system across several reasoning dimensions.



# System Weaknesses

Limited negation detection

Weak temporal reasoning

Incorrect subject attribution

Incomplete metadata extraction

# Proposed Improvements

Add negation detection rules

Improve temporal context detection

Implement family history classification

Add metadata validation checks

# Conclusion

The evaluation framework provides a structured way to measure the reliability of clinical entity extraction systems.
By identifying common error patterns, it helps improve the trustworthiness and robustness of healthcare AI pipelines.

Repository Structure
repo/
│
├── output/
│   ├── chart_01.json
│   ├── chart_02.json
│
├── report.md
└── test.py
