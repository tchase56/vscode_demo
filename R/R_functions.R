library(ggplot2)
library(ggcorrplot)

calculate_andPlot_correlation <- function(data_df){
    #' Corrlation
    #'
    #' Calculates the corrlation matrix of the data and creates visualization
    #'
    #' @param data_df input tibble used to create correlation matrix
    
    # Correlation matrix
    corr <- round(cor(data), 1)
    print(head(corr))

    # Plot
    ggcorrplot(
        corr,
        hc.order = TRUE,
        lab = TRUE,
        lab_size = 3,
        method = "circle",
        colors = c("tomato2", "white", "springgreen3"),
        title = "Correlation of wine data",
        ggtheme=theme_bw
    )
}