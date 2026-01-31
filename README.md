# hylreg_PCL

PCL（Point Cloud Library）相关项目仓库。本仓库为 **demo** 工作区，内含多个子项目。使用 [uv](https://docs.astral.sh/uv/) 管理依赖与工作区。

## 子项目

| 路径 | 说明 |
|------|------|
| [demo/open_pointcloud](demo/open_pointcloud/) | 打开点云并显示（支持 .ply / .pcd / .xyz 等） |

## 环境

- Python 3.10+
- uv

## 使用

**推荐**：进入子项目目录后再安装与运行。

```bash
cd demo/<子项目名>
uv sync
uv run python main.py
```

若在仓库根目录操作：

```bash
uv sync
uv run --package <包名> <入口命令>
```

各子项目详细说明见其目录下的 `README.md`。
