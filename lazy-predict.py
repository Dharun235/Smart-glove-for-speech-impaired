"""Compare baseline classifiers for a prepared five-sensor Excel dataset."""

import argparse

import pandas as pd
from lazypredict.Supervised import LazyClassifier
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler


def main() -> None:
    """Load data, train LazyPredict baselines, and print the score table."""
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("dataset", help="Excel file with five sensor columns and a label column")
    parser.add_argument("--label-column", default="label")
    args = parser.parse_args()

    dataframe = pd.read_excel(args.dataset)
    features = dataframe.iloc[:, :5]
    if args.label_column not in dataframe:
        raise ValueError(f"Missing label column: {args.label_column}")
    target = dataframe[args.label_column]
    x_train, x_test, y_train, y_test = train_test_split(
        features, target, test_size=0.2, random_state=42, stratify=target
    )

    scaler = StandardScaler()
    x_train = scaler.fit_transform(x_train)
    x_test = scaler.transform(x_test)
    classifier = LazyClassifier(ignore_warnings=True, custom_metric=None)
    models, _ = classifier.fit(x_train, x_test, y_train, y_test)
    print(models)


if __name__ == "__main__":
    main()
