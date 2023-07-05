clear;clc;
%导入功能连接矩阵的node的label文件
%labeling = load('/Users/fan/Documents/Data/zhouTestData/label.mat');
root_dir = '/Users/qingchen/Documents/Data/Twin_2015_FC/FC_mat';
out_path = '/Users/qingchen/Documents/Data/Twin_2015_FC/gradient_m';
if ~exist(out_path,'dir')
    mkdir(out_path);
end
data_all = dir([root_dir filesep 'sub-*']);
disp(data_all)
for sub = 1:numel(data_all)
   sub_func = load([root_dir filesep data_all(sub).name '/func_gordonsubcortical.mat']); 
   gm = GradientMaps('kernel','normalizedAngle','approach','diffusionEmbedding');
   gm = gm.fit(sub_func.data);
   out_name = [out_path filesep data_all(sub).name];
   if~exist(out_name,'dir')
       mkdir(out_name);
   end
   save([out_name '/gredient.mat'],'gm'); 
   sub
end
