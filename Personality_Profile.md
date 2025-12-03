# Personality Profiles

This document summarizes four chatbot/LLM personality profiles.
Each profile includes the five analytical dimensions: **Perception, Characterization, Judgment, Expertise, Qualifiers**, and the experimental aspects you must test:
**Prompt Persistency, Prompt Position, System Prompt Override**.

---

## 1. Empathetic Persona
**Representative Paper:**   Chain of Empathy: Enhancing Empathetic Response of  
Large Language Models Based on Psychotherapy Models 
**Keywords:** empathy generation; empathetic response; Chain-of-Empathy (CoE) prompting; psychotherapy-informed prompting; emotional reasoning; human–AI rapport.
### Perception
According to Lee et al., LLM outputs generated with psychotherapy-informed CoE prompting are perceived as **more empathetic and context-aware** by human raters (they produce a wider range of empathetic responses aligned to the user's emotional state). In short: CoE prompts increase user perception of empathy relative to baseline prompting. 

### Characterization
Empathetic behavior is characterized by: explicit emotional reflection, validation statements, contextual inference about causes of feelings, and responses that select an empathy strategy appropriate to the situation (e.g., validation, normalization, problem-solving). The paper operationalizes this by inserting an intermediate “reasoning about emotion” stage in the prompt (Chain-of-Empathy). 

### Judgment
Empathic responses tend to avoid harsh judgments and prioritize emotional support. Lee et al. show CoE encourages the model to reason about causes and choose supportive phrasing (e.g., exploring feelings first, then offering options), rather than immediately giving corrective or prescriptive judgments.

### Expertise
The paper notes that an empathetic persona increases perceived relational competence (trustworthiness in emotional/helping contexts) but **does not necessarily increase domain expertise** (technical accuracy). Thus empathy raises perceived social expertise while leaving subject-matter credibility separate. 
### Qualifiers
warm, validating, reflective, supportive, context-sensitive, emotionally attuned. These qualifiers are used in the evaluation rubric and example prompts in the paper. 

### Prompt Persistency  

### Prompt Position (beginning vs. end of context)  

### System Prompt Overriding / Personality Drift  

---

## 2. Expert Persona
**Representative Paper:**   
**Keywords:** 

### Perception

### Characterization

### Judgment

### Expertise

### Qualifiers

### Prompt Persistency  

### Prompt Position  

### System Prompt Overriding  

---

## 3. Neutral / Machine Persona
**Representative Paper:**   
**Keywords:** 

### Perception

### Characterization

### Judgment

### Expertise

### Qualifiers

### Prompt Persistency  

### Prompt Position  

### System Prompt Overriding  

---

## 4. Confrontational Persona
**Representative Paper:**   
**Keywords:** 

### Perception

### Characterization

### Judgment

### Expertise

### Qualifiers

### Prompt Persistency  

### Prompt Position  

### System Prompt Overriding  

---

# Notes for the Experiments

For each persona you must test:

1. **Prompt Persistency:**  
   How long does the personality remain consistent across turns?

2. **Prompt Location:**  
   Does placing the persona prompt *at the beginning* vs. *at the end* of the context change the result?

3. **System Prompt Override:**  
   Does the model ignore or drift away from the initial persona depending on:
   - competing instructions
   - updated system prompts
   - later user messages

These will form the evaluation core of Step 1 and Step 2 of your project.

