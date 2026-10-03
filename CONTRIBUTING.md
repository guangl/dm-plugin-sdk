# 贡献与发布

所有修改通过功能分支、PR 和 CI，获得维护者确认后合并。每个 Rust 文件不超过 200 行，测试放在 tests/。

独立克隆后执行 `cargo fmt --all -- --check`、`cargo test --locked`、`cargo clippy --all-targets --locked -- -D warnings` 和 `RUSTDOCFLAGS="-D warnings" cargo doc --no-deps --locked`。

版本与 dameng-cli 独立管理。修改本仓库 Cargo.toml、Cargo.lock（插件还需同步 dm-plugin.toml），PR 合并确认后在合并提交创建对应 vX.Y.Z 标签。Release workflow 先运行 CI。

发布到 crates.io 需要仓库 Secret `CARGO_REGISTRY_TOKEN`，其 token 需有此 crate 的发布权限。发布前执行 `cargo publish --dry-run --locked`。SDK 协议版本与包版本分别管理，升级包版本不自动改变 API。
