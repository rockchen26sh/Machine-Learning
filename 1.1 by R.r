
training_data <- read.table('C:/Users/chenshengkang/Documents/GitHub/Machine Learning/datingTestSet2.txt',header = FALSE)

head(training_data)
colnames(training_data)<- c('licheng','game','ice','label')

plot(training_data[,1:3])
plot(training_data[,1:2])
library(ggplot2)
ggplot(training_data,aes(x=licheng,y=game,color=label))+geom_point()

normData1 <- (training_data[,1] - min(training_data[,1]))/(max(training_data[,1])-min(training_data[,1]))
normData2 <- (training_data[,2] - min(training_data[,2]))/(max(training_data[,2])-min(training_data[,2]))
normData3 <- (training_data[,3] - min(training_data[,3]))/(max(training_data[,3])-min(training_data[,3]))
normData <- data.frame(licheng=normData1,game=normData2,ice=normData3,training_data[4])

ggplot(normData,aes(x=licheng,y=game,color=label))+geom_point()
