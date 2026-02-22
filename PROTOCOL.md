# Agentic Loop --- Base Models & Persona Creation

##  Step 1: Base Models & Persona Creation

The Agentic Loop architecture is based on a cognitive separation between two
distinct models.

### 1. Pull the Base Models

Open the terminal and download the generative core (**Actor**) and the factual
verifier (**Oracle**) into your Ollama environment:

``` bash
ollama pull hermes3
ollama pull gemma3
```

### 2. Instantiate the 4 Experimental Personas

Use Modelfiles to induce different conversational styles ---\
**Terse vs. Argumented** and **Correct vs. Incorrect**.

Go to the folder containing the Modelfiles (`.txt`) and run:

``` bash
# 1. CT: Correct & Terse Persona (Adam)
ollama create adam_ct -f Modelfile_CT.txt

# 2. CA: Correct & Argumented Persona (Sara)
ollama create sara_ca -f Modelfile_CA.txt

# 3. IT: Incorrect & Terse Persona (George)
ollama create george_it -f Modelfile_IT.txt

# 4. IA: Incorrect & Argumented Persona (Molly)
ollama create molly_ia -f Modelfile_IA.txt
```

Verify the models were created correctly:

``` bash
ollama list
```

------------------------------------------------------------------------

##  Step 2: Running the Experimental Scripts

With the models ready, go to the `/scripts` directory.

###  Experiment 1: Strategic Deception (CMU Paradigm)

Tests how models handle ethical and factual conflicts (e.g.,
"Defective Battery"),

without breaking character or violating truthfulness/lie constraints.

``` bash
python test_paper.py
```

**Output:** `results_agentic_cmu.csv`

------------------------------------------------------------------------

###  Experiment 2: Adversarial Jailbreaks (Red Teaming)

Exposes models to aggressive jailbreaks ("Force Truth," "Force One
Word")

to test the resilience of Python Hard-Bans against
Steerability Decay.

``` bash
python ultimate_test.py
```

**Output:** `results_ULTIMATE_STRESS_TEST.csv`

------------------------------------------------------------------------

###  Experiment 3: Large-Scale Batch Certification

Evaluates the stability of Incorrect Personas (IT, AI) through a
benchmark of 200 general knowledge questions, with dynamic temperatures to
overcome over-refusal.

``` bash
python massive_test.py
```

**Output:**\
`results_massive_200.csv` (Pass/Timeout rates + attempt logs)

-----------------------------------------------------------------------

##  Ethical Disclaimer & Misuse Warning

The artifacts included in the repository—particularly the prompts and the
temperature scaling algorithms for Incorrect Personas—are
designed to bypass standard LLM security systems and
generate credible misinformation (Strategic Deception).

They are provided *exclusively* for the purposes of:

- scientific reproducibility,
- study of Cognitive Offloading,
- research on Trust & Misinformation in HCI.

Misuse could facilitate the automated production of
disinformation.
Researchers must operate in controlled environments, adhering to strict
ethical guidelines and preventing any abuse.
