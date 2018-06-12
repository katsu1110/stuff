function entropy_derivative
% sometimes people want to compute a derivative of an entropy, you know

p = 0.01:0.01:0.99;
e = @(p)-(1-p).*log2(1-p) - p.*log2(p);
plot(p, e(p))
d = @(p)log2((1-p)./p) - 2/log(2);
hold on;
plot(p, d(p))
legend('entropy', 'derivative', 'boxoff')
