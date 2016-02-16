execute pathogen#infect()
autocmd StdinReadPre * let s:std_in=1
autocmd VimEnter * if argc() == 0 && !exists("s:std_in") | NERDTree | endif

nmap <F8> :TagbarToggle<CR>

"colorscheme
syntax enable
colorscheme solarized
set background=dark
set t_Co=256  

"General
set ruler "shows line and column of the cursor"
set tabstop=4 "tab 4 spaces"
set shiftwidth=4 "number of spaces to use when auto indent
set expandtab
set smartindent
set showmatch

