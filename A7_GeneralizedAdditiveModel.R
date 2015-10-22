library(gam)
setwd("/Users/vamshiguduguntla/Downloads")
data <- read.csv(file = "LAdata.csv" , header = T)

#Fitting linear model
m1<-lm(data$Deaths~data$O2 +data$SO2+data$NO2 +data$CO)
r <- m1$residual
#Added variable plots to look for non-linearity
plot(data$O2,r)
lo    <- loess(r~data$O2)
summary(lo)
lines(lo$x[order(data$O2)],lo$fit[order(data$O2)],col=2,lwd=2)
####Has an NL relationship


plot(data$SO2,r)
lo    <- loess(r~data$SO2)
summary(lo)
lines(lo$x[order(data$SO2)],lo$fit[order(data$SO2)],col=2,lwd=2)
####Has an NL relationship


plot(data$NO2,r)
lo    <- loess(r~data$NO2)
summary(lo)
lines(lo$x[order(data$NO2)],lo$fit[order(data$NO2)],col=2,lwd=2)
####Has a Linear relationship


plot(data$CO,r)
lo    <- loess(r~data$CO)
summary(lo)
lines(lo$x[order(data$CO)],lo$fit[order(data$CO)],col=2,lwd=2)
####Has a Non Linear relationship

fit1 <- gam(data$Deaths~data$O2 +data$SO2+data$NO2 +data$CO+data$RelHumid+data$Temp)
summary(fit1)

m1<-gam(data$Deaths~s(data$O2) +s(data$SO2)+data$NO2 +s(data$CO) +s(data$O2,data$SO2))
summary(m1)
  
