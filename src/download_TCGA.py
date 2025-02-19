import pandas as pd
import os


def get_manifest_path():
    script_dir = os.path.dirname(os.path.abspath(__file__))
    project_root = os.path.dirname(script_dir)
    manifest_path = os.path.join(project_root, "data", "gdc-manifest.txt")
    return manifest_path

def create_batches(df, max_batch_size_gb=50):
    batches = []
    current_batch = []
    current_size = 0
    
    for c, row in df.iterrows():
        if current_size + row["size_gb"] > max_batch_size_gb:
            if current_batch:
                batches.append(current_batch)
            current_batch = [row]
            current_size = row["size_gb"]
        else:
            current_batch.append(row)
            current_size += row["size_gb"]

    if current_batch:
        batches.append(current_batch)

    return batches




def main():
    df = pd.read_csv(get_manifest_path(), sep="\t")
    #print(df.head())
    #print(df.columns)
    df["size_gb"] = df["size"] / (1024 ** 3)
    batches = create_batches(df)
    print(df.head())
    print(f"Created {len(batches)} batches")

if __name__ == "__main__":
    main()

