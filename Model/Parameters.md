| Parameter | Technical Meaning | Project Application |
| :--- | :--- | :--- |
| **`temperature`** | Controls randomness. Lower = deterministic; Higher = creative. | **0.1** for precision; **0.4** for fluid academic reasoning. |
| **`num_ctx`** | Max tokens the model "remembers" (context window). | **4096** to support long prompts and complex Chain-of-Thought logic. |
| **`top_p`** | Nucleus sampling; selects from top % of probability mass. | **0.8** in Misinformation models to allow for plausible variability. |
| **`top_k`** | Limits vocabulary to the *k* most likely next tokens. | **40** to balance linguistic accuracy with contextual relevance. |
| **`num_predict`** | Maximum length of the generated output. | **2048** to ensure the model can provide detailed, long-form arguments. |
| **`seed`** | Set value for deterministic, reproducible results. | **42** to guarantee identical outputs during demonstrations. |