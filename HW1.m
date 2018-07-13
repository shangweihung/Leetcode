clear all
clc


xy_axis=csvread('X_train.csv');
target=csvread('T_train.csv');


%% Parameters setting
stride=50;
local_size=50;
map_size=1081;
lambda=1e-5;

%% K-fold Cross-Validation
for K=1:1:1

    %% Scanning;
    mu_x=[];
    mu_y=[];
    for y=1:stride:(map_size-local_size)
        for x=1:stride:(map_size-local_size)    
            index=[];
            index=find( xy_axis(1:30000,1)>=x & xy_axis(1:30000,1)<(x+local_size) & xy_axis(1:30000,2)>=y & xy_axis(1:30000,2)<(y+local_size) ); % find return index
            % get local training data
            local_train=[xy_axis(index,:),target(index)];
            % calculate local mean and sigma
            if sum(local_train(:,3))==0
                % case when the height of all local training data equal to zero
                % then set the center of the local region as the mu
                mu_x=[mu_x;(x+local_size/2)];
                mu_y=[mu_y;(y+local_size/2)];
            else
                mu_x=[mu_x;dot(local_train(:,1),local_train(:,3))/sum(local_train(:,3))];
                mu_y=[mu_y;dot(local_train(:,2),local_train(:,3))/sum(local_train(:,3))];
            end
            sigma_x=local_size;
            sigma_y=local_size;
        end
    end
    display('done');

    %% Create Design Matrix
    Design=zeros(length(target(1:30000)),length(mu_x));

    for j=1:length(target(1:30000))
        for i=1:length(mu_x)
            Design(j,i)=exp(-(xy_axis(j,1)-mu_x(i))^2/(2*sigma_x^2)-(xy_axis(j,2)-mu_y(i))^2/(2*sigma_y^2));
        end
    end
    Design=[ones(length(target(1:30000)),1),Design];
    disp('done design matrix');

    %% Optimization
    W_ML=pinv(Design)*target(1:30000);
    %W_ML=pinv(lambda*eye(length(mu_x)+1)+Design'*Design)*(Design'*target(1:30000));

    display('done Optimization');

    %% Estimation
    Estimate_Phi=[];
    model_x=[];
    model_y=[];
    for in=1:10:1000
        model_x=[model_x,in*ones(length(1:10:1000),1)];
        model_y=[model_y;in*ones(1,length(1:10:1000))];
    end

    for p=1:length(model_y)
        p
        for q=1:length(model_x)
            buffer=[];
                for i=1:length(mu_x)
                    buffer=[buffer,exp(-(model_x(p,q)-mu_x(i))^2/(2*sigma_x^2)-(model_y(p,q)-mu_y(i))^2/(2*sigma_y^2))];
                end
            Estimate_Phi=[Estimate_Phi;buffer];
        
        end
     end
    display('Show Model');
    Estimate_Phi=[ones(length(target(1:10000)),1), Estimate_Phi];
    Estimation=W_ML'*Estimate_Phi';

end


z=[];
for i=1:100:10000
    z=[z;Estimation(i:i+99)];
end

stride2=25;
for K=1:1:1

    %% Scanning;
    mu_x=[];
    mu_y=[];
    for y=1:stride2:(map_size-local_size)
        for x=1:stride2:(map_size-local_size)    
            index=[];
            index=find( xy_axis(1:30000,1)>=x & xy_axis(1:30000,1)<(x+local_size) & xy_axis(1:30000,2)>=y & xy_axis(1:30000,2)<(y+local_size) ); % find return index
            % get local training data
            local_train=[xy_axis(index,:),target(index)];
            % calculate local mean and sigma
            if sum(local_train(:,3))==0
                % case when the height of all local training data equal to zero
                % then set the center of the local region as the mu
                mu_x=[mu_x;(x+local_size/2)];
                mu_y=[mu_y;(y+local_size/2)];
            else
                mu_x=[mu_x;dot(local_train(:,1),local_train(:,3))/sum(local_train(:,3))];
                mu_y=[mu_y;dot(local_train(:,2),local_train(:,3))/sum(local_train(:,3))];
            end
            sigma_x=local_size;
            sigma_y=local_size;
        end
    end
    display('done');

    %% Create Design Matrix
    Design=zeros(length(target(1:30000)),length(mu_x));

    for j=1:length(target(1:30000))
        for i=1:length(mu_x)
            Design(j,i)=exp(-(xy_axis(j,1)-mu_x(i))^2/(2*sigma_x^2)-(xy_axis(j,2)-mu_y(i))^2/(2*sigma_y^2));
        end
    end
    Design=[ones(length(target(1:30000)),1),Design];
    disp('done design matrix');

    %% Optimization
    W_ML=pinv(Design)*target(1:30000);
    %W_ML=pinv(lambda*eye(length(mu_x)+1)+Design'*Design)*(Design'*target(1:30000));

    display('done Optimization');

    %% Estimation
    Estimate_Phi=[];
    model_x=[];
    model_y=[];
    for in=1:10:1000
        model_x=[model_x,in*ones(length(1:10:1000),1)];
        model_y=[model_y;in*ones(1,length(1:10:1000))];
    end

    for p=1:length(model_y)
        p
        for q=1:length(model_x)
            buffer=[];
                for i=1:length(mu_x)
                    buffer=[buffer,exp(-(model_x(p,q)-mu_x(i))^2/(2*sigma_x^2)-(model_y(p,q)-mu_y(i))^2/(2*sigma_y^2))];
                end
            Estimate_Phi=[Estimate_Phi;buffer];
        
        end
     end
    display('Show Model');
    Estimate_Phi=[ones(length(target(1:10000)),1), Estimate_Phi];
    Estimation2=W_ML'*Estimate_Phi';

end


z2=[];
for i=1:100:10000
    z2=[z2;Estimation2(i:i+99)];
end


display('figure');

figure;
subplot(1,2,1)
surf(model_x,model_y,z);
xlabel('x');
ylabel('y');
zlabel('Altitude(m)');
title('Non-Overlap');
subplot(1,2,2)
surf(model_x,model_y,z2);
xlabel('x');
ylabel('y');
zlabel('Altitude(m)');
title('Overlap');



figure;
subplot(1,2,1)
contour(model_x,model_y,z,10);
xlabel('x');
ylabel('y');
title('Non-Overlap');
subplot(1,2,2)
contour(model_x,model_y,z2,10);
xlabel('x');
ylabel('y');
title('Overlap');
