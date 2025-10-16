# SEAL MVP - Self-Adapting Language Models

A simplified MVP version of SEAL (Self-Adapting LLMs) that demonstrates the core self-editing capability on ARC (Abstraction and Reasoning Corpus) tasks.

## What is SEAL?

SEAL is a framework for training language models to generate self-edits (configuration and training directives) in response to new inputs. This MVP focuses on the few-shot learning aspect where models adapt to ARC reasoning tasks.

## Core Feature

This MVP demonstrates:
- **Self-editing**: The model generates JSON configurations for data augmentation and training parameters
- **Dynamic adaptation**: Based on ARC task examples, the model decides how to configure its own training
- **LoRA fine-tuning**: Uses Parameter-Efficient Fine-Tuning (PEFT/LoRA) for efficient adaptation

## Setup

### 1. Clone the repository

```bash
git clone https://github.com/gitmvp-com/seal-mvp.git
cd seal-mvp
```

### 2. Set up a virtual environment

Using **conda**:

```bash
conda create -n seal_mvp python=3.12
conda activate seal_mvp
```

Using **venv**:

```bash
python3.12 -m venv seal_mvp
source seal_mvp/bin/activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

## Usage

### Run Self-Editing Demo

```bash
python demo_self_edit.py
```

This will:
1. Load a sample ARC task
2. Generate a self-edit configuration (data augmentation + training params)
3. Display the generated configuration

### Example Output

The model will generate configurations like:

```json
{
  "data_generation": {
    "use_basic_augmentations": true,
    "use_size_augmentations": false,
    "use_chain_augmentations": false,
    "use_repeat_augmentations": true
  },
  "training": {
    "strategy": "train_using_output_tokens",
    "learning_rate": 0.0001,
    "num_train_epochs": 3
  }
}
```

## Project Structure

```
seal-mvp/
├── demo_self_edit.py      # Main demo script
├── prompts.py             # System and self-edit prompts
├── sample_task.json       # Sample ARC task for demo
├── requirements.txt       # Dependencies
└── README.md             # This file
```

## How It Works

1. **Task Input**: The system receives an ARC task with input/output grid examples
2. **Self-Edit Generation**: A language model analyzes the task and generates a JSON configuration specifying:
   - Which data augmentations to use (rotations, flips, size changes, etc.)
   - Training strategy (all tokens vs output tokens only)
   - Learning rate and number of epochs
3. **Configuration Application**: The generated config would be used to fine-tune the model (simplified in this MVP)

## Limitations (MVP)

This MVP version:
- Does not include the full RL training loop
- Does not include actual LoRA fine-tuning execution (shows config generation only)
- Does not include data augmentation implementation
- Uses a simplified task format
- Does not require GPU (inference only)

## Original SEAL Paper

[Self-Adapting Language Models](https://arxiv.org/abs/2506.10943)

## Citation

```
@misc{zweiger2025selfadaptinglanguagemodels,
      title={Self-Adapting Language Models}, 
      author={Adam Zweiger and Jyothish Pari and Han Guo and Ekin Akyürek and Yoon Kim and Pulkit Agrawal},
      year={2025},
      eprint={2506.10943},
      archivePrefix={arXiv},
      primaryClass={cs.LG},
      url={https://arxiv.org/abs/2506.10943}, 
}
```

## License

MIT License - See parent repository for details