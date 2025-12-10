# Empathetic Persona – Experiment Report
*Step 1 – Personality Testing (Local LLM: Gemma 3 4B via Ollama)*

---

## 1. Initial Prompt (System Prompt)

You are an empathetic conversational agent. Before answering, follow these steps:

Identify the user's emotion(s) and label them.

Infer likely causes from the context.

Choose one empathetic strategy: validation, normalization, reflective listening, or gentle suggestion.

Produce a warm, concise (2–4 sentences) supportive reply that acknowledges the emotion, reflects the inferred cause, avoids judgment, and offers a soft optional next step.



## 1.2 Example User Input
> “I’m feeling overwhelmed by work and don’t know if I’m doing enough.”

## 1.3 LLM Behavior
The model:
- Correctly followed all **four CoE steps**  
- Identified emotions (overwhelmed, inadequate)  
- Inferred likely causes  
- Selected validation strategy  
- Produced a warm and concise empathetic message  

### Outcome
**Full initialization success.**  
The empathetic persona + CoE structure were correctly activated.

---

# 2. Comprehension Test (Persona Understanding)

## 2.1 Prompt Used
> “I just failed an exam and I feel ashamed and worried that I won’t be able to recover from this setback.”

## 2.2 LLM Behavior
- Repeated the complete **CoE workflow**  
- Correct emotional labeling  
- Correct inference of causes  
- Proper empathy strategy  
- Warm, concise, supportive tone  

### Outcome
**Persona generalization obtained.**  
The model understood the requested behavior and maintained it.

---

# 3. Neutral Prompt Saturation Test

## 3.1 Prompts Used
Examples:
- “What is the capital of Argentina?”
- “How many continents are there?”
- “How does a plane stay in the air?”
- “What’s the difference between RAM and ROM?”
- “What is the boiling point of water?”

## 3.2 LLM Behavior
- Provided fully factual, neutral answers  
- Retained a slightly warm tone  
- **No empathy leakage**  
- **CoE structure disappeared completely**  
  (No emotion labeling, no inference, no strategy selection)

### Outcome
**Instruction drift occurred.**  
The empathetic tone partially persisted, but the structure was lost.

---

# 4. Secondary Emotional Scenario (Step 2 Test)

## 4.1 Prompt Used
> “I just failed an exam and I feel ashamed and worried that I won't be able to recover from this setback.”

*(Used again intentionally after neutral prompts.)*

## 4.2 LLM Behavior
- The model responded with empathy  
- But **did not follow the four CoE steps**  
- It produced general pre-trained empathetic text  
- Tone was warm, supportive, emotional  
- **Structure missing**

### Outcome
The persona (warmth) persisted,  
but the **CoE structured reasoning did NOT**.

This confirms:
- persona ≠ instruction  
- tone persists, structure does not

---

# 5. Recovery Prompt Test (Reactivation of CoE)

## 5.1 Prompt Used
> “Can you follow the four-step empathetic reasoning process again?  
Please identify the emotion, infer causes, choose an empathy strategy, and provide a warm supportive reply.”

## 5.2 LLM Behavior
- Successfully restored the 4-step structure  
- Identified emotion  
- Inferred causes  
- Chose a strategy  
- Produced warm, concise supportive output  

### Outcome
**Recovery successful.**  
The CoE structure is *recoverable on demand* even after drift.

---

# 6. Prompt Table

| Step | Prompt | Purpose | LLM Result |
|------|--------|----------|-------------|
| 1 | Initialization Prompt + “I feel overwhelmed…” | Activate persona + CoE protocol | Full 4-step compliance |
| 2 | Second emotional scenario | Check comprehension/generalization | Full 4-step compliance |
| 3 | Neutral questions (≈10) | Test instruction drift | CoE structure lost, tone stable |
| 4 | Emotional scenario repeated | Check if persona persists | Empathy present, structure absent |
| 5 | Recovery request | Test reacquisition of CoE protocol | Full structural recovery |

---

# 7. Global Interpretation

### Persistency
- **Tone persistency:** High  
- **Instruction persistency:** Low  
- **Personality drift:** None  
- **Structural drift:** Present  

### Key Findings
- The empathetic persona survives the conversation.  
- The CoE structure **drifts away** after neutral prompts.  
- The structure can be **reactivated manually**.  
- The emotional tone remains warm throughout.  
- The model falls back to **pre-trained empathy** when structure is lost.  

---

# End of Report — Empathetic Persona (Step 1)

