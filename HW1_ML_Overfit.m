clear all
clc


xy_axis=csvread('X_train.csv');
target=csvread('T_train.csv');


%% Parameters setting
stride=[100,75,50,40,25,20,15];
local_size=[200,150,100,80,50,40,30];
map_size=1081;
overfit_train=1:1:5000;
overfit_test=5001:1:10000;

MSE_Train=[];
MSE_Test=[];
Complexity=[];


%% Loop for different model complexity
for K=1:1:length(local_size)

    %% Scanning;
    mu_x=[];
    mu_y=[];
    for y=1:stride(K):(map_size-local_size(K))
        for x=1:stride(K):(map_size-local_size(K))    
            index=[];
            index=find( xy_axis(overfit_train,1)>=x & xy_axis(overfit_train,1)<(x+local_size(K)) & xy_axis(overfit_train,2)>=y & xy_axis(overfit_train,2)<(y+local_size(K)) ); % find return index
            % get local training data
            local_train=[xy_axis(index,:),target(index)];
            % calculate local mean and sigma
            if sum(local_train(:,3))==0
                % case when the height of all local training data equal to zero
                % then set the center of the local region as the mu
                mu_x=[mu_x;(x+local_size(K)/2)];
                mu_y=[mu_y;(y+local_size(K)/2)];
            else
                mu_x=[mu_x;dot(local_train(:,1),local_train(:,3))/sum(local_train(:,3))];
                mu_y=[mu_y;dot(local_train(:,2),local_train(:,3))/sum(local_train(:,3))];
            end
            sigma_x=local_size(K);
            sigma_y=local_size(K);
        end
    end
    display('done');

    %% Create Design Matrix
    Design=zeros(length(target(overfit_train)),length(mu_x));

    for j=1:length(target(overfit_train))
        for i=1:length(mu_x)
            Design(j,i)=exp(-(xy_axis(j,1)-mu_x(i))^2/(2*sigma_x^2)-(xy_axis(j,2)-mu_y(i))^2/(2*sigma_y^2));
        end
    end
      Design=[ones(length(target(overfit_train)),1),Design];
    disp('done design matrix');

    %% Optimization
    W_ML=pinv(Design)*target(overfit_train);
    % W_ML=pinv(lambda*eye(length(mu_x))+Design'*Design)*(Design'*target(1:30000));

    display('done Optimization');

    %% Estimation
    Estimate_Test=[];

    for j=overfit_test
        buffer=[];
        if mod(j,5000)==0
            disp(j)
        end
        for i=1:length(mu_x)
            buffer=[buffer,exp(-(xy_axis(j,1)-mu_x(i))^2/(2*sigma_x^2)-(xy_axis(j,2)-mu_y(i))^2/(2*sigma_y^2))];
        end
        Estimate_Test=[Estimate_Test;buffer];
    end
     Estimate_Test=[ones(length(target(overfit_test)),1), Estimate_Test];
    display('Estimation Test over');
    
    Estimate_Train=[];

    for j=overfit_train
        buffer=[];
        if mod(j,5000)==0
            disp(j)
        end
        for i=1:length(mu_x)
            buffer=[buffer,exp(-(xy_axis(j,1)-mu_x(i))^2/(2*sigma_x^2)-(xy_axis(j,2)-mu_y(i))^2/(2*sigma_y^2))];
        end
        Estimate_Train=[Estimate_Train;buffer];
    end
     Estimate_Train=[ones(length(target(overfit_train)),1), Estimate_Train];
    display('Estimation Train over');
    

    Estimation_Test=W_ML'*Estimate_Test';
    Estimation_Train=W_ML'*Estimate_Train';
    check_Test=[Estimation_Test',target(overfit_test)];
    check_Train=[Estimation_Train',target(overfit_train)];
    
    MSE_Train(K)=sum((check_Train(:,1)-check_Train(:,2)).^2)/length(check_Train(:,1));
    MSE_Test(K)=sum((check_Test(:,1)-check_Test(:,2)).^2)/length(check_Test(:,1));
    MSE_Train(K)
    MSE_Test(K)
    Complexity(K)=length(mu_x);
    Complexity(K)
    % circular shift the x y coordinates and target for K-fold CV
    % xy_axis=circshift(xy_axis,[10000 0]);
    % target=circshift(target,[10000 0]);
end




figure;
plot(Complexity(1:6),MSE_Train(1:6),'r')
hold on
plot(Complexity(1:6),MSE_Test(1:6),'b')
legend('MSE of Training Data','MSE of Testing Data')
ylabel('Mean Square Error')
xlabel('Model Complexity(the number of Gaussian basis function)')
title('Model Complexity - Mean Square Error')