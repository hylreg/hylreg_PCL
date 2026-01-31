# Demo 目录

存放各类 PCL 小 demo，每个 demo 为 workspace 子项目（独立 `pyproject.toml`）。与 hylreg_QT、hylreg_OpenCV 结构一致。

## 当前 demo

| 文件夹 | 说明 |
|--------|------|
| `open_pointcloud` | 打开点云文件并显示（支持 .ply / .pcd / .xyz 等；不传路径则显示示例点云） |

## 运行方式

进入对应子项目目录后执行：

```bash
uv sync
uv run python main.py
```

各子项目说明见其目录下的 `README.md`。
