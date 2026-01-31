# 打开点云

使用 Open3D 打开点云文件并显示，或生成示例点云。支持 `.ply`、`.pcd`、`.xyz` 等格式。

## 运行

在**本目录**下执行：

```bash
uv sync
uv run python main.py
# 或指定点云文件
uv run python main.py /path/to/pointcloud.ply
```

或使用入口命令：

```bash
uv run open-pointcloud
uv run open-pointcloud /path/to/pointcloud.pcd
```

不传文件路径时会显示一个示例立方体点云。

关闭窗口或按 **Q** 退出。

## 依赖

- Open3D（点云读写与可视化）
