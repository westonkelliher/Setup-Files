
;; melpa for downloading packages
;;(require 'package)
;;(add-to-list 'package-archives
;;             '("melpa" . "https://melpa.org/packages/") t)
;;(package-initialize)
;;(package-refresh-contents)


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
(package-initialize)

(global-unset-key (kbd "C-q")) ;; to use as special key for tmux
(global-set-key (kbd "M-q") 'quoted-insert) ;; replace quoted insert

(global-unset-key (kbd "C-z")) ;; so that we can use my jikm config within emacs
(global-set-key (kbd "C-z h") 'split-window-below)
(global-set-key (kbd "C-z v") 'split-window-right)
(global-set-key (kbd "C-z k") 'windmove-right)
(global-set-key (kbd "C-z j") 'windmove-left)
(global-set-key (kbd "C-z i") 'windmove-up)
(global-set-key (kbd "C-z m") 'windmove-down)
(global-set-key (kbd "C-z x") 'delete-window)

(global-set-key (kbd "C-x %") 'query-replace)
(global-set-key (kbd "M-p") 'backward-paragraph)
(global-set-key (kbd "M-n") 'forward-paragraph)
(global-set-key (kbd "C-c C-t") 'ansi-term)

(global-set-key (kbd "C-c C-x") 'kmacro-bind-to-key)

;; -*- mode: elisp -*-

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
 '(package-selected-packages (quote (rust-mode))))
(custom-set-faces
 ;; custom-set-faces was added by Custom.
 ;; If you edit it by hand, you could mess it up, so be careful.
 ;; Your init file should contain only one such instance.
 ;; If there is more than one, they won't work right.
 )


(fset 'expand-for-loop
   "\C-a\C-i\C-[dfor (int \C-y = 0; \C-y <\C-e; \C-y++) {\C-m\C-m}\C-p\C-i")
(global-set-key (kbd "C-c f") 'expand-for-loop)
