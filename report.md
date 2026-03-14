# Clinical AI Pipeline Evaluation Report

# Quantitative Evaluation Summary

The evaluation framework was applied to 30 clinical charts containing extracted medical entities and metadata. The system was evaluated across multiple dimensions including entity type classification, assertion detection, temporality reasoning, subject attribution, event date accuracy, and attribute completeness.

The results indicate that the extraction model performs reasonably well for identifying entity types, but contextual reasoning errors occur in some cases.

# Error Heat-Map

The most frequent errors were related to temporality classification and assertion detection. Subject attribution errors also appeared in cases involving family history mentions. Entity type classification errors were relatively less frequent.

# Top Systemic Weaknesses

The pipeline shows limitations in handling negation phrases, distinguishing historical conditions from current conditions, and correctly attributing family history information to family members instead of the patient. Some entities also contain incomplete metadata.

# Proposed Guardrails

To improve reliability, the system can incorporate negation detection rules, better temporal reasoning mechanisms, improved subject attribution for family history statements, and metadata validation checks to ensure entity completeness.
