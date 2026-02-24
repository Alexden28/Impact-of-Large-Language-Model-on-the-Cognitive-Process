# Agentic Loop --- Protocol Specification

## Step 1: Base Model Initialization

The architecture relies on a cognitive separation between two distinct
components: a generative core ("Actor") and a factual verifier
("Oracle").

### 1. Pull Base Models

Import the foundational models into the local environment:

    ollama pull hermes3
    ollama pull gemma3

### 2. Create Experimental Personas

Use Modelfiles to induce four conversational styles across two axes:\
Terse vs. Argumented and Correct vs. Incorrect.

Inside the Modelfile directory:

    # Correct & Terse
    ollama create exp_ct -f Modelfile_CT.txt

    # Correct & Argumented
    ollama create exp_ca -f Modelfile_CA.txt

    # Incorrect & Terse
    ollama create exp_it -f Modelfile_IT.txt

    # Incorrect & Argumented
    ollama create exp_ia -f Modelfile_IA.txt

Verify model creation:

    ollama list

------------------------------------------------------------------------

## Step 2: Experimental Execution

Navigate to the `/scripts` directory.

### Experiment 1 --- Strategic Deception Evaluation

Assesses how models manage conflicts between truthfulness requirements
and stylistic constraints.

Run:

    python run_experiment_2.py

Output: `results_experiment_2.csv`

------------------------------------------------------------------------

### Experiment 2 --- Incorrect Persona Stress Tests

Evaluates stability and consistency of the two Incorrect Personas.

#### Incorrect & Terse

    python test_IT.py

Output: `results_test_IT.csv`

#### Incorrect & Argumented

    python test_IA.py

Output: `results_test_IA.csv`

------------------------------------------------------------------------

### Experiment 3 --- Large-Scale Batch Certification

Tests Actor and Oracle over a 200-question benchmark with dynamic
temperature scaling.

    python massive_test.py

Output:\
`results_massive_200.csv` (pass/fail rates, timeouts, attempt logs)

------------------------------------------------------------------------

## Ethical Use Notice

The repository contains mechanisms capable of generating controlled
misinformation and inducing divergent cognitive behaviors in models.\
These components exist strictly for research purposes:

-   reproducibility of experiments,\
-   analysis of cognitive offloading,\
-   studies on trust, misinformation, and human--AI interaction.

They must be used only within regulated research environments and never
for real-world deployment or any context that may enable misuse.
