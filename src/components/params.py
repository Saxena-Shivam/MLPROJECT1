params={
    "Decision Tree" :{
        "criterion":['squared_error','friedman_mse','absolute_error','poisson'],
        "splitter":['best','random'],
        # "max_depth":[2,3,4,5,6,7,8,9,10],
        # "min_samples_split":[2,3,4,5,6,7,8,9,10],
        # "min_samples_leaf":[1,2,3,4,5,6,7,8,9,10]
    },
    "Random Forest" :{
        "n_estimators":[100,200,300,400,500],
        "criterion":['squared_error','friedman_mse','absolute_error','poisson'],
        # "max_depth":[2,3,4,5,6,7,8,9,10],
        # "min_samples_split":[2,3,4,5,6,7,8,9,10],
        # "min_samples_leaf":[1,2,3,4,5,6,7,8,9,10]
    },
    "Gradient Boosting" :{
        "loss":['squared_error','huber','absolute_error','quantile'],
        "learning_rate":[0.1,0.01,0.05,0.001],
        # "n_estimators":[100,200,300,400,500],
        # "subsample":[0.6,0.7,0.75,0.8,0.85,0.9],
        # "criterion":['squared_error','friedman_mse','absolute_error','poisson'],
        # "max_depth":[2,3,4,5,6,7,8,9,10],
        # "min_samples_split":[2,3,4,5,6,7,8,9,10],
        # "min_samples_leaf":[1,2,3,4,5,6,7,8,9,10]
    },
    "Linear Regression" :{},
    "K-Neighbors Regressor" :{
        "n_neighbors":[5,7,9,11,13,15],
        "weights":['uniform','distance'],
        "metric":['euclidean','manhattan']
    },
    "XGBRegressor" :{
        "learning_rate":[0.1,0.01,0.05,0.001],
        # "n_estimators":[100,200,300,400,500],
        # "max_depth":[2,3,4,5,6,7,8,9,10],
        # "min_child_weight":[1,2,3,4,5],
        # "gamma":[0.0,0.1,0.2,0.3],
        # "colsample_bytree":[0.6,0.7,0.75,0.8,0.85]
    },
    "CatBoosting Regressor" :{
        "depth":[6,8,10],
        # "learning_rate":[0.01,0.05,0.1],
        # "iterations":[100,200,300]
    },
    "AdaBoost Regressor" :{
        "n_estimators":[100,200,300,400,500],
        # "learning_rate":[0.01,0.05,0.1,0.001]
    }
    
}