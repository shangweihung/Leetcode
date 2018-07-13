
z=[];
for i=1:100:10000
    z=[z;Estimation(i:i+99)];
end

display('figure');

figure;
contour(model_x,model_y,z,10);