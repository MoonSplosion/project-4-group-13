# project-4-group-13
Overview
This project is an exploration and analysis of Pokémon data, focusing on the comparison of stats across generations and types, as well as an attempt to predict catch rates using machine learning. By creating interactive dashboards and employing a machine learning model, we aimed to answer key questions about Pokémon characteristics and performance in battles. The project also highlighted some limitations, particularly with the reliability of the catch rate data.

Key Features
Interactive Dashboards:

Dashboard 1: Provides line charts that visualize the overall average stats of Pokémon across eight generations. Users can compare average attack, defense, speed, special attack, and special defense, making it easier to target specific generations for strategic purposes.
Dashboard 2: Features a horizontal bar chart displaying the number of Pokémon for each type, from water to flying, and a bubble chart showing the average height and weight for each type. This enables users to explore the distribution and physical characteristics of different Pokémon types.
Machine Learning Model:

We employed the Random Forest Regressor to predict Pokémon catch rates based on the dataset's attributes. The model produced a Root Mean Square Error (RMSE) of 66%, demonstrating good predictive performance compared to other models tested. Despite this, challenges in the data’s reliability impacted the model's performance.
Analysis and Findings
Generational Stats Comparison:
Our first dashboard revealed that the seventh generation Pokémon have the highest average attack, defense, special attack, and special defense, making them potentially the most effective in battles. Fourth generation Pokémon, on the other hand, ranked highest in speed.
Pokémon Type Distribution:
From the second dashboard, we found that water-type Pokémon are the most common, while flying-type Pokémon are the least represented. This insight into the distribution of types provides valuable information for those strategizing team compositions.
Challenges
Catch Rate Data
One significant challenge we faced was with the "catch rate" data. Initially, it appeared that each Pokémon had a simple, predetermined catch rate. However, we discovered that the catch rate is influenced by a complex formula that accounts for external factors like weather conditions and the type of Poké Ball used. As a result, the catch rate data provided in the dataset was unrealistic and unreliable for predictive purposes. This issue affected the accuracy of our model and emphasized the importance of using accurate, real-world data in future projects.

Dataset Limitations
Generation Information: The original dataset lacked a column for Pokémon generations. To overcome this, we imported a secondary dataset to add this essential information.
Model Deployment Issues: We encountered version incompatibility and data type mismatches during model deployment, which underscored the importance of ensuring all dependencies are aligned before going live.
Conclusion
This project provided valuable insights into Pokémon statistics and type distributions, revealing key generational and type-based patterns. However, the limitations of the dataset, particularly regarding the catch rate, highlighted the importance of using reliable data for accurate predictions. The experience emphasized the need for data integrity and alignment of tools and dependencies when building machine learning models.