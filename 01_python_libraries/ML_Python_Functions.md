
# Machine Learning – Python Functions Cheat Sheet

My quick reference guide for important Python libraries and functions used in Machine Learning.

## 1. NumPy (np)
Purpose: Numerical computations, arrays and matrices.

| Function | Description |
|---|---|
| np.array() | Create an array |
| np.arange() | Generate a sequence |
| np.zeros() | Create an array of zeros |
| np.ones() | Create an array of ones |
| np.reshape() | Change array shape |
| np.mean() | Calculate mean |
| np.median() | Calculate median |
| np.std() | Calculate standard deviation |
| np.sum() | Calculate sum |
| np.max() | Find maximum |
| np.min() | Find minimum |
| np.dot() | Calculate dot product |
| np.concatenate() | Join arrays |

## 2. Pandas (pd)
Purpose: Data manipulation and analysis.

| Function | Description |
|---|---|
| pd.DataFrame() | Create DataFrame |
| pd.Series() | Create Series |
| pd.read_csv() | Read CSV file |
| df.head() | Display first five rows |
| df.tail() | Display last five rows |
| df.info() | Dataset information |
| df.describe() | Statistical summary |
| df.shape | Number of rows and columns |
| df.columns | Display column names |
| df.isnull() | Identify missing values |
| df.dropna() | Remove missing values |
| df.fillna() | Fill missing values |
| df.duplicated() | Identify duplicate rows |
| df.drop_duplicates() | Remove duplicates |
| df.groupby() | Group data |
| df.sort_values() | Sort data |

## 3. Matplotlib (plt)
Purpose: Data visualization.

| Function | Description |
|---|---|
| plt.plot() | Line graph |
| plt.scatter() | Scatter plot |
| plt.bar() | Bar graph |
| plt.hist() | Histogram |
| plt.xlabel() | X-axis label |
| plt.ylabel() | Y-axis label |
| plt.title() | Graph title |
| plt.legend() | Display legend |
| plt.grid() | Display grid |
| plt.figure() | Create figure |
| plt.subplot() | Create multiple plots |
| plt.show() | Display graph |

## 4. Seaborn (sns)
Purpose: Statistical data visualization.

| Function | Description |
|---|---|
| sns.scatterplot() | Relationship between variables |
| sns.lineplot() | Line visualization |
| sns.barplot() | Statistical bar plot |
| sns.histplot() | Data distribution |
| sns.boxplot() | Identify outliers |
| sns.heatmap() | Correlation visualization |
| sns.pairplot() | Pairwise relationships |
| sns.countplot() | Count categorical values |
| sns.load_dataset() | Load sample datasets |

## 5. Scikit-learn (sklearn)
Purpose: Machine Learning algorithms and model building.

| Function / Class | Description |
|---|---|
| train_test_split() | Split training and testing data |
| LinearRegression() | Linear Regression |
| LogisticRegression() | Logistic Regression |
| DecisionTreeClassifier() | Decision Tree |
| KNeighborsClassifier() | KNN classification |
| StandardScaler() | Feature standardization |
| MinMaxScaler() | Feature normalization |
| LabelEncoder() | Encode categorical labels |
| OneHotEncoder() | One-hot encoding |
| accuracy_score() | Calculate accuracy |
| confusion_matrix() | Evaluate classification |
| mean_squared_error() | Calculate regression error |
| r2_score() | Evaluate regression |

## 6. Important ML Model Methods

| Method | Description |
|---|---|
| model.fit(X, y) | Train the model |
| model.predict(X) | Make predictions |
| model.score(X, y) | Calculate model score |
| model.transform(X) | Transform data |

## 7. Basic Machine Learning Workflow

1. Load dataset – Pandas
2. Process data – NumPy and Pandas
3. Visualize data – Matplotlib and Seaborn
4. Split dataset – train_test_split()
5. Train model – model.fit()
6. Make predictions – model.predict()
7. Evaluate model – Appropriate evaluation metrics

## Learning Goal

Build a strong foundation in Python libraries and learn to implement Machine Learning algorithms independently.
