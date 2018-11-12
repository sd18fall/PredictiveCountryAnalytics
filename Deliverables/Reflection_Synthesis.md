# Architecture Review Reflection and Synthesis Document
## Feedback and decisions

 Based upon your notes from the technical review, synthesize the feedback you received addressing your key questions. How do you plan to incorporate it going forward? What new questions did you generate?
* General approach to completing this project: The two big points of concern are the ML and the GUI. We’ve decided to split the two tasks evenly and run with them, while working in the same space and discussing while working in order to keep integrating our work together. GUI will be developed on a website through HTML and Javascript. Sara has an interest in website design and will pursue this task. 
* GeoCharts by Google is a simple Javascript library that we plan to utilize. The Machine Learning backend for our project is the other large unknown. The comment that we should look into Principle Component Analysis (PCA) was useful and we plan to look into that further. 
* We received a lot of questions about what our coefficient was and what it meant. We plan to mitigate this issue by making the coefficient less noticeable and display the true variable values alongside the coefficient. In addition, we will put a blurb on the webpage explaining our “coefficient” calculation.

## Review process reflection 
How did the review go? Did you get answers to your key questions? Did you provide too much/too little context for your audience? Did you stick closely to your planned agenda, or did you discover new things during the discussion that made you change your plans? What could you do next time to have an even more effective technical review?

* Yes, we did get answers to our key questions. Through the architectural review, we learned two important tools we can use in our project. It was brought to our knowledge that the modsimpy library includes the functionality of scraping data from the World Bank, which is critical to getting data for our machine learning model. We will also be using GeoCharts by Google in the mapping of our data. 
* I think we provided a good amount of context for our audience. We allocated three minutes to the background and context and stuck to our plan. In those three minutes, we were able to effectively convey the scope of our project and the architectural components of the project. 
* Although we allocated an equal amount to both the GUI and ML portions, we found that most people in the class were not very familiar with ML. As a result, we spent more time discussing the components of the GUI.

