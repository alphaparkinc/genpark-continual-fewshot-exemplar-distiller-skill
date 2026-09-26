import sys
if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8")

from client import ContinualFewshotExemplarDistillerClient

def main():
    client = ContinualFewshotExemplarDistillerClient()
    res = client.distill_fewshot_exemplars()
    print("=== Continual Fewshot Exemplar Distiller Output ===")
    print(f"Domain: {res['task_domain']} | Selected: {res['exemplars_selected_for_prompt']} exemplars")
    print(f"Learning Gain: {res['continual_learning_gain_score']*100}% | Status: {res['curation_status']}")
    print("\nDistilled Few-Shot Demonstrations:")
    for ex in res['distilled_fewshot_demonstrations']:
        print(f"  * Q: "{ex['example_input']}"")
        print(f"    A: "{ex['canonical_output']}" (Score: {ex['confidence']})")

if __name__ == '__main__':
    main()
