# Conventional Commits 指南

這份文件說明本專案撰寫 commit 訊息時所遵循的 Conventional Commits 規範，確保版本歷史一致且易於自動化處理（例如產生發版紀錄）。

## 基本格式
```
type(optional scope): concise statement

(optional body)

(optional footer)
```
- `type`：必要欄位，描述這次變更的性質。
- `scope`：可選，指出受影響的模組或目錄，建議使用小寫 kebab-case，例如 `docs`, `matrix`, `tests`。
- `concise statement`：一句話說清楚這次做了什麼，使用祈使句（例："add matrix identity demo"）。
- `body`：可選，補充動機、作法或與先前版本的差異。
- `footer`：可選，用於紀錄議題編號或 BREAKING CHANGE。

## 常用 type
| type | 用途 | 範例 |
|------|------|------|
| `feat` | 新功能或使用者可見的改變 | `feat: add matrix identity demo script` |
| `fix`  | 修正 bug | `fix: handle empty matrix input` |
| `docs` | 文件與註解 | `docs: explain conventional commits rules` |
| `style` | 程式碼風格，無行為更動 | `style: reformat matrix helpers` |
| `refactor` | 重構，行為不變 | `refactor: extract multiply helper` |
| `perf` | 效能提升 | `perf: cache shape validation` |
| `test` | 測試新增或調整 | `test: cover transpose edge cases` |
| `build` | 建置系統、相依套件 | `build: bump numpy version` |
| `ci` | CI/CD 設定 | `ci: run lint on pull requests` |
| `chore` | 例行雜事，不影響程式 | `chore: tidy gitignore entries` |
| `revert` | 還原前次 commit | `revert: "feat: add matrix identity demo script"` |

## BREAKING CHANGE
若這次變更會讓使用 API 的人需要修改程式，必須在 footer 註明：
```
BREAKING CHANGE: describe what changed and what to do
```

## 實作建議步驟
1. 在進行修改前確認想新增或修正的內容屬於哪種 type。
2. 編輯完成後使用 `git status` 檢查 staged 檔案是否正確。
3. 撰寫 commit 訊息時遵守上述格式，避免使用口語或過度冗長的描述。
4. 多個變更類型務必拆成多個 commit，維持歷史乾淨。

## 範例
```
feat(matrix): add dot product demo script

- 實作 Frobenius 內積
- 透過 trace(A^T * B) 驗證定義
```
```
docs: add README usage instructions
```

依照這套規範撰寫 commit，可讓團隊清楚了解每次改動的目的，也方便未來自動產生 changelog 或統計資料。
