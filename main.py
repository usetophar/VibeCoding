from pathlib import Path

import pandas as pd


def main():
    base_dir = Path(__file__).resolve().parent
    xml_path = base_dir / "drugs.xml"
    csv_path = base_dir / "drugs.csv"

    dataframe = pd.read_xml(xml_path, xpath=".//item", parser="etree")
    dataframe.to_csv(csv_path, index=False, encoding="utf-8-sig")

    print(f"Converted {xml_path.name} to {csv_path.name}")


if __name__ == "__main__":
    main()
