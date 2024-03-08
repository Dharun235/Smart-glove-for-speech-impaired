from lazypredict.Supervised import LazyClassifier
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
import pandas as pd

# Replace 'your_encoded_data_file.xlsx' with the actual file path
encoded_data_file_path = 'concatenated_data1.xlsx'  # Replace with your actual file path

# Read the Excel file into a DataFrame
df = pd.read_excel(encoded_data_file_path)

# Features (finger positions)
X = df.iloc[:, :5]

# Target variable (single column with binary numbers representing classes)
y = df['label']  # Replace 'your_target_column_name' with the actual column name

# Split the data into training and testing sets (70% train, 30% test)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Use StandardScaler for normalization
scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)

# Use Lazy Predict to automatically select and evaluate models
clf = LazyClassifier(ignore_warnings=True, custom_metric=None)
models, predictions = clf.fit(X_train_scaled, X_test_scaled, y_train, y_test)

# Display the model performance summary
print(models)

