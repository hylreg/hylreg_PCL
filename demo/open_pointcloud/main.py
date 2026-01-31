"""打开点云并显示的 demo。支持从文件加载或生成示例点云。按 'Q' 或关闭窗口退出。"""
import argparse
import sys
from pathlib import Path

import open3d as o3d


def load_or_create_point_cloud(path: str | None) -> o3d.geometry.PointCloud:
    if path:
        p = Path(path)
        if not p.exists():
            print(f"文件不存在: {path}")
            sys.exit(1)
        pcd = o3d.io.read_point_cloud(str(p))
        if not pcd.has_points():
            print(f"无法读取点云或文件为空: {path}")
            sys.exit(1)
        return pcd
    # 无路径时生成示例点云（一个简单立方体表面采样）
    print("未指定文件，显示示例点云（立方体）")
    mesh = o3d.geometry.TriangleMesh.create_box(width=1.0, height=1.0, depth=1.0)
    mesh.translate((-0.5, -0.5, -0.5))
    pcd = mesh.sample_points_uniformly(number_of_points=2000)
    return pcd


def main() -> None:
    parser = argparse.ArgumentParser(description="打开点云并显示（支持 .ply / .pcd / .xyz 等）")
    parser.add_argument(
        "path",
        nargs="?",
        default=None,
        help="点云文件路径（可选；不填则显示示例点云）",
    )
    args = parser.parse_args()

    pcd = load_or_create_point_cloud(args.path)
    print("点云点数:", len(pcd.points))
    print("关闭窗口或按 Q 退出")
    o3d.visualization.draw_geometries(
        [pcd],
        window_name="Point Cloud Demo",
        width=800,
        height=600,
    )


if __name__ == "__main__":
    main()
