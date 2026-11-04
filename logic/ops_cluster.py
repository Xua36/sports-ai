import pandas as pd
from sklearn.cluster import KMeans
import os

def run_user_clustering(data_path):
    """对用户进行简单的 K-Means 聚类（基于年龄和体能）"""
    df = pd.read_csv(data_path, encoding='gbk')
    
    # 准备聚类特征（年龄、体能等级）
    X = df[['age', 'fitness_level']]
    
    # 设定聚为 3 类
    kmeans = KMeans(n_clusters=3, random_state=42, n_init=10)
    df['cluster'] = kmeans.fit_predict(X)
    
    # 给聚类打上业务标签
    cluster_names = {}
    for i in range(3):
        cluster_data = df[df['cluster'] == i]
        avg_age = cluster_data['age'].mean()
        avg_fit = cluster_data['fitness_level'].mean()
        
        if avg_age > 45:
            cluster_names[i] = "中老年健步群体"
        elif avg_fit > 3.5:
            cluster_names[i] = "青年高体能路跑群体"
        else:
            cluster_names[i] = "大众娱乐休闲群体"
            
    df['group_name'] = df['cluster'].map(cluster_names)
    return df, df['group_name'].value_counts()