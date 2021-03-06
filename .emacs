
;; melpa for downloading packages
;;(require 'package)
;;(add-to-list 'package-archives
;;             '("melpa-stable" . "https://stable.melpa.org/packages/"))
;;(package-initialize)
;;(package-refresh-contents)
;;(set package-check-signature nil)

;;(use-package flycheck
;;  :hook (prog-mode . flycheck-mode))

;;(use-package company
;;  :hook (prog-mode . company-mode)
;;  :config (setq company-tooltip-align-annotations t)
;;          (setq company-minimum-prefix-length 1))

;;(use-package lsp-mode
;;  :commands lsp
;;  :config (require 'lsp-clients))

;;(use-package lsp-ui)


;; Added by Package.el.  This must come before configurations of
;; installed packages.  Don't delete this line.  If you don't want it,
;; just comment it out by adding a semicolon to the start of the line.
;; You may delete these explanatory comments.
;;(package-initialize)


;; hooks
(defun enable-hs-minor-mode ()
  "Turn on `hs-minor-mode' mode."
  (interactive)
  (hs-minor-mode 1))
(add-hook 'c-mode-hook 'enable-hs-minor-mode)

;;(global-unset-key (kbd "C-q")) ;; to use as special key for tmux
;;(global-set-key (kbd "M-q") 'quoted-insert) ;; replace quoted insert

;; I'm using normal emacs multiplexing commands but I still don't like accidentally closing
;; emacs when I don't have a tmux ession running
(global-unset-key (kbd "C-z")) ;; so that we can use my jikm config within emacs

(global-set-key (kbd "C-z h") 'split-window-below)
(global-set-key (kbd "C-z v") 'split-window-right)
(global-set-key (kbd "C-z k") 'windmove-right)
(global-set-key (kbd "C-z j") 'windmove-left)
(global-set-key (kbd "C-z i") 'windmove-up)
(global-set-key (kbd "C-z m") 'windmove-down)
(global-set-key (kbd "C-z x") 'delete-window)

;;(global-set-key (kbd "C-h") 'delete-backward-char)
(global-set-key (kbd "C-x %") 'query-replace)
(global-set-key (kbd "M-p") 'backward-paragraph)
(global-set-key (kbd "M-n") 'forward-paragraph)
(global-set-key (kbd "C-c C-t") 'ansi-term)
(global-set-key (kbd "C-c %") 'query-replace-regexp)

(global-set-key (kbd "C-c C-x") 'kmacro-bind-to-key)

(global-set-key (kbd "C-c h") 'hs-hide-block)
(global-set-key (kbd "C-c s") 'hs-show-block)
(global-set-key (kbd "C-c H") 'hs-hide-all)
(global-set-key (kbd "C-c S") 'hs-show-all)


;; Disable the splash screen (to enable it agin, replace the t with 0)
(setq inhibit-splash-screen t)

;; Enable transient mark mode
(transient-mark-mode 1)

;;;;Org mode configuration
;; Enable Org mode
(require 'org)
;; Make Org mode work with files ending in .org
;; (add-to-list 'auto-mode-alist '("\\.org$" . org-mode))
;; The above is the default in recent emacsen
(custom-set-variables
 ;; custom-set-variables was added by Custom.
 ;; If you edit it by hand, you could mess it up, so be careful.
 ;; Your init file should contain only one such instance.
 ;; If there is more than one, they won't work right.
 '(package-selected-packages (quote (gnu-elpa-keyring-update markdown-mode rust-mode)))
 '(send-mail-function (quote sendmail-send-it)))
(custom-set-faces
 ;; custom-set-faces was added by Custom.
 ;; If you edit it by hand, you could mess it up, so be careful.
 ;; Your init file should contain only one such instance.
 ;; If there is more than one, they won't work right.
 )



(setq c-basic-offset 4)



(fset 'expand-for-loop
   "\C-a\C-i\C-[dfor (int \C-y = 0; \C-y <\C-e; \C-y++) {\C-m\C-m}\C-p\C-i")
(global-set-key (kbd "C-c f") 'expand-for-loop)

(fset 'kill-line-left
   "\C-@\C-p\C-e\C-w\C-m")
(global-set-key (kbd "C-c k") 'kill-line-left)

(fset 'kill-to-end-of-last-line
   (lambda (&optional arg) "Keyboard macro." (interactive "p") (kmacro-exec-ring-item (quote (" " 0 "%d")) arg)))
(global-set-key (kbd "C-c w") 'kill-to-end-of-last-line)
(put 'upcase-region 'disabled nil)

;;(fset 'line-cutoff
;;      "\C-a\C-[7\C-[0\C-f\C-[f\C-[b")
;;(global-set-key (kbd "C-c e") 'line-cutoff)

(fset 'smart_line_end_70
   "\C-a\C-[7\C-[0\C-f\C-r \C-f\C-b\C-[b\C-[f\C-s \C-f\C-b")
(global-set-key (kbd "C-c E") 'smart_line_end_70)

(fset 'smart_line_end_80
   "\C-a\C-[8\C-[0\C-f\C-r \C-f\C-b\C-[b\C-[f\C-s \C-f\C-b")
(global-set-key (kbd "C-c e") 'smart_line_end_80)


(defun blank-active-region (beg end)
  "Replace space with CHAR in the region."
  (interactive
   (if (use-region-p)
       (list
	(region-beginning)
	(region-end))
     (user-error "No useable region")))
  (insert
   (replace-regexp-in-string
    "[^[:space:]\n]"
    " "
        (delete-and-extract-region beg end))))

(fset 'cutoff_line_80
      "\C-a\C-[f\C-r \C-f\C-@\C-a\C-w\C-y\C-ce\C-m\C-@\C-a\C-w\C-y\C-[y\C-@\C-a\C-[xbla\C-in\C-i\C-m\C-e\C-p\C-e")
(global-set-key (kbd "C-c RET") 'cutoff_line_80)

(fset 'into_text_1
   "' +  + '\C-b\C-b\C-b\C-b")
(global-set-key (kbd "C-c '") 'into_text_1)

(fset 'into_text_2
   "\" +  + \"\C-b\C-b\C-b\C-b")
(global-set-key (kbd "C-c \"") 'into_text_2)
