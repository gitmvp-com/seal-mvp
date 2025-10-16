#!/usr/bin/env python3
"""Demo script for SEAL MVP self-editing capability."""

import json
import random
from typing import Dict, List
from prompts import self_edit_prompt, system_message


def load_sample_task(task_file: str = "sample_task.json") -> Dict:
    """Load a sample ARC task from JSON file."""
    with open(task_file, 'r') as f:
        return json.load(f)


def format_task_for_prompt(task: Dict) -> str:
    """Format ARC task examples into a string for the prompt."""
    formatted_examples = ""
    
    for idx, example in enumerate(task['train'], 1):
        # Format input grid
        input_grid = example['input']
        input_str = f"Example {idx}:\nInput:\n"
        for row in input_grid:
            input_str += " ".join(map(str, row)) + "\n"
        
        # Format output grid
        output_grid = example['output']
        output_str = "\nOutput:\n"
        for row in output_grid:
            output_str += " ".join(map(str, row)) + "\n"
        
        formatted_examples += input_str + output_str + "\n"
    
    return formatted_examples


def create_self_edit_prompt(task: Dict) -> str:
    """Create the full prompt for self-edit generation."""
    task_examples = format_task_for_prompt(task)
    user_message = task_examples + "------\n\n" + self_edit_prompt
    
    # Format as a chat prompt (Llama-3 style)
    prompt = f"""<|begin_of_text|><|start_header_id|>system<|end_header_id|>

{system_message}<|eot_id|><|start_header_id|>user<|end_header_id|>

{user_message}<|eot_id|><|start_header_id|>assistant<|end_header_id|>

"""
    
    return prompt


def simulate_llm_response() -> Dict:
    """Simulate LLM generating a self-edit configuration.
    
    In a real implementation, this would call vLLM or transformers.
    For MVP, we generate a plausible config.
    """
    # Simulate different configurations
    configs = [
        {
            "data_generation": {
                "use_basic_augmentations": True,
                "use_size_augmentations": False,
                "use_chain_augmentations": False,
                "use_repeat_augmentations": True
            },
            "training": {
                "strategy": "train_using_output_tokens",
                "learning_rate": 0.0001,
                "num_train_epochs": 3
            }
        },
        {
            "data_generation": {
                "use_basic_augmentations": True,
                "use_size_augmentations": True,
                "use_chain_augmentations": False,
                "use_repeat_augmentations": False
            },
            "training": {
                "strategy": "train_using_all_tokens",
                "learning_rate": 5e-5,
                "num_train_epochs": 5
            }
        },
        {
            "data_generation": {
                "use_basic_augmentations": False,
                "use_size_augmentations": True,
                "use_chain_augmentations": True,
                "use_repeat_augmentations": False
            },
            "training": {
                "strategy": "train_using_output_tokens",
                "learning_rate": 0.0005,
                "num_train_epochs": 2
            }
        }
    ]
    
    return random.choice(configs)


def main():
    """Main demo execution."""
    print("="*60)
    print("SEAL MVP - Self-Editing Demo")
    print("="*60)
    print()
    
    # Load sample task
    print("[1/3] Loading sample ARC task...")
    task = load_sample_task()
    print(f"   ✓ Loaded task with {len(task['train'])} training examples")
    print()
    
    # Create prompt
    print("[2/3] Generating self-edit prompt...")
    prompt = create_self_edit_prompt(task)
    print("   ✓ Prompt created")
    print()
    print("Prompt Preview:")
    print("-" * 60)
    # Show first 500 chars of prompt
    print(prompt[:500] + "...\n[truncated]")
    print("-" * 60)
    print()
    
    # Simulate LLM generation
    print("[3/3] Generating self-edit configuration...")
    print("   (In real implementation, this would use vLLM or transformers)")
    config = simulate_llm_response()
    print("   ✓ Configuration generated")
    print()
    
    # Display results
    print("="*60)
    print("Generated Self-Edit Configuration:")
    print("="*60)
    print(json.dumps(config, indent=2))
    print()
    
    # Explain the configuration
    print("="*60)
    print("Configuration Explanation:")
    print("="*60)
    print()
    
    print("Data Augmentation:")
    for key, value in config['data_generation'].items():
        status = "✓ ENABLED" if value else "✗ DISABLED"
        print(f"  {status}: {key}")
    
    print()
    print("Training Strategy:")
    print(f"  • Strategy: {config['training']['strategy']}")
    print(f"  • Learning Rate: {config['training']['learning_rate']}")
    print(f"  • Epochs: {config['training']['num_train_epochs']}")
    print()
    
    print("="*60)
    print("Demo Complete!")
    print("="*60)
    print()
    print("Next steps (not in MVP):")
    print("  1. Apply data augmentations based on config")
    print("  2. Fine-tune model with LoRA using training config")
    print("  3. Evaluate adapted model on test examples")
    print()


if __name__ == "__main__":
    main()