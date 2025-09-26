# Codex CLI 常用指令速查

這份文件整理我在使用 Codex CLI 時最常呼叫的指令，方便快速回憶用途與注意事項。

## 對話控制
- `/init`：在目前工作目錄啟動新會話，Codex 會回報沙箱模式、授權策略、網路權限等環境資訊。若切換專案或想重置上下文，重新輸入一次即可。
- `/model`：顯示目前會話使用的模型。若環境支援切換，也可以在後面加模型代號，例如 `/model gpt-5-preview`。

## 授權與沙箱
- `/proval`：管理需要授權的指令。當 shell 命令被沙箱擋下時，Codex 會提示使用 `/proval approve <id>` 或 `/proval deny <id>`；`/proval status` 可以檢視所有待處理項目。若 `approval_policy` 設為 `never`，這組指令會被鎖住。

## 命令歷程
- `/history`：列出最近互動的摘要，包含已執行的指令與 Codex 回覆，方便檢視流程與複製命令。
- `/clear`：清掉目前終端的對話記錄，只影響畫面，不會重置會話狀態。

## 其他常見操作
- `/help`：顯示 CLI 支援的所有指令與簡短說明。
- `/exit`：結束 Codex CLI 程式，離開後會話就會終止。

> 提醒：以 `/` 開頭的是 CLI 控制指令，不會送到模型。要執行 shell 命令仍然使用 `!` 或直接輸入系統指令，例如 `bash -lc "ls"`。記得確認目前的 `sandbox_mode` 與 `approval_policy`，以免命令被阻擋。
