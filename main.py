import pathlib

def create_sample_data_file(filepath):
    """Creates a sample data file with various valid and malformed entries."""
    content = """
# This is a list of users and their ages.
Alice,30
Bob,15
Charlie,22
David,
Eve,19
Frank,abc
Grace,45,extra
Henry,17
    """
    filepath.write_text(content.strip(), encoding='utf-8')
    print(f"Created sample data file: {filepath.name}")

def simulate_ai_agent_task(filepath, goal_description):
    """
    Simulates a simple AI agent attempting to fulfill a data processing goal.
    This demonstrates how an AI agent might struggle with ambiguous requirements,
    malformed data, or unexpected formats, requiring human oversight or
    explicit clarification beyond simple code generation.
    """
    print(f"Agent's Goal: {goal_description}")
    print(f"Attempting to process file: {filepath.name}\n")

    adult_users = []
    processed_count = 0
    skipped_count = 0

    try:
        with filepath.open('r', encoding='utf-8') as f:
            for line_num, raw_line in enumerate(f, 1):
                line = raw_line.strip()

                # --- AI Agent's interpretation and processing logic ---
                # A human developer would easily infer to ignore comments and empty lines.
                # An AI agent needs explicit rules or robust pattern recognition to do so.
                if not line or line.startswith('#'):
                    continue

                parts = line.split(',')
                if len(parts) == 2:
                    name = parts[0].strip()
                    age_str = parts[1].strip()
                    try:
                        age = int(age_str)
                        if age >= 18:
                            adult_users.append(name)
                        processed_count += 1
                    except ValueError:
                        # This is a common point where an AI might fail without specific instructions.
                        # A human would ask: "How should I handle non-numeric ages?" The agent here just skips.
                        print(f"  [Agent Observation] Line {line_num}: Cannot parse age '{age_str}' for '{name}'. Skipping entry.")
                        skipped_count += 1
                else:
                    # Another point of failure: unexpected line format.
                    # A human would ask: "What should I do with lines that don't have exactly two parts?"
                    print(f"  [Agent Observation] Line {line_num}: Unexpected format '{line}'. Expected 'Name,Age'. Skipping entry.")
                    skipped_count += 1
                # --- End of AI Agent's interpretation and processing logic ---

    except FileNotFoundError:
        print(f"Error: File '{filepath.name}' not found.")
        return []
    except Exception as e:
        print(f"An unexpected error occurred during processing: {e}")
        return []

    print(f"\nProcessed {processed_count} valid entries, skipped {skipped_count} entries due to format/parsing issues.")
    return adult_users

def main():
    data_filename = "user_data.txt"
    data_filepath = pathlib.Path(data_filename)

    create_sample_data_file(data_filepath)

    goal = "Identify and list the names of all users who are 18 years or older from the provided data file. The file contains 'Name,Age' entries. Ignore comments and empty lines."

    result = simulate_ai_agent_task(data_filepath, goal)

    print("\n--- Agent's Final Report ---")
    if result:
        print("Identified adult users:")
        for user in result:
            print(f"- {user}")
    else:
        print("No adult users found or an error occurred.")

    # Clean up the created file
    data_filepath.unlink(missing_ok=True)
    print(f"\nCleaned up sample data file: {data_filepath.name}")

if __name__ == "__main__":
    main()