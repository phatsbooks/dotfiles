"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""               
"               
"               ██╗   ██╗██╗███╗   ███╗██████╗  ██████╗
"               ██║   ██║██║████╗ ████║██╔══██╗██╔════╝
"               ██║   ██║██║██╔████╔██║██████╔╝██║     
"               ╚██╗ ██╔╝██║██║╚██╔╝██║██╔══██╗██║     
"           ███╗ ╚████╔╝ ██║██║ ╚═╝ ██║██║  ██║╚██████╗
"           ╚══╝  ╚═══╝  ╚═╝╚═╝     ╚═╝╚═╝  ╚═╝ ╚═════╝
"               
"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""               

" GENERAL SETTINGS ------------------------------------------------------- {{{
" Disable compatibility with vi which can cause unexpected issues.
set nocompatible

" Enable type file detection. Vim will be able to try to detect the type of file is use.
filetype on

" Enable plugins and load plugin for the detected file type.
filetype plugin on

" Load an indent file for the detected file type.
filetype indent on

" Turn syntax highlighting on.
syntax on

" Add numbers to the file.
set number

" Set shift width to 4 spaces.
set shiftwidth=4

" Highlight matching brackets
set showmatch

" Set tab width to 4 columns.
set tabstop=4

" Use space characters instead of tabs.
set expandtab

" Do not save backup files.
set nobackup

set cursorline
set nocursorcolumn

" Do not let cursor scroll below or above N number of lines when scrolling.
set scrolloff=10

" Do not wrap lines. Allow long lines to extend as far as the line goes.
set nowrap

" While searching though a file incrementally highlight matching characters as you type.
set incsearch

" Ignore capital letters during search.
set ignorecase

" Override the ignorecase option if searching for capital letters.
" This will allow you to search specifically for capital letters.
set smartcase

" Show partial command you type in the last line of the screen.
set showcmd

" Show the mode you are on the last line.
set showmode

" Show matching words during a search.
set showmatch

" Use highlighting when doing a search.
set hlsearch

" Set the commands to save in history default number is 20.
set history=1000

" Enable auto completion menu after pressing TAB.
set wildmenu

" Make wildmenu behave like similar to Bash completion.
set wildmode=list:longest

" Set split default direction
set splitbelow splitright

" Set true colors
set termguicolors

" There are certain files that we would never want to edit with Vim.
" Wildmenu will ignore files with these extensions.
set wildignore=*.docx,*.jpg,*.png,*.gif,*.pdf,*.pyc,*.exe,*.flv,*.img,*.xlsx

" Set unicode encoding
set encoding=utf8

set mouse=a
" }}}

" COMMANDS --------------------------------------------------------------- {{{

command! -nargs=0 Prettier :CocCommand prettier.formatFile

command! -nargs=* T split | resize 12 | terminal <args>

" }}} 

" MAPPINGS --------------------------------------------------------------- {{{

" Set the backslash as the leader key.
let mapleader = ","

" Leader key for Emmet vim
let g:user_emmet_leader_key='\'
let g:user_emmet_install_global = 0
autocmd FileType html,css,javascript EmmetInstall

" Turn off search highlighting
nnoremap <leader>, :nohlsearch<CR>

" Press ,\ to jump back to the last cursor position.
nnoremap <leader>\ ``

" Source this .vimrc quickly
nnoremap <leader>s :w :source %<CR>

" Press \p to print the current file to the default printer from a Linux operating system.
" View available printers:   lpstat -v
" Set default printer:       lpoptions -d <printer_name>
" <silent> means do not display output.
nnoremap <silent> <leader>p :%w !lp<CR>

" Type jj to exit insert mode quickly.
inoremap jj <Esc>

" Press the space bar to type the : character in command mode.
nnoremap <nowait> <space> :

" Pressing the letter o will open a new line below the current one.
" Exit insert mode after creating a new line above or below the current line.
"nnoremap o o<esc>
"nnoremap O O<esc>

" Center the cursor vertically when moving to the next word during a search.
nnoremap n nzz
nnoremap N Nzz

" Yank from cursor to the end of line.
nnoremap Y y$

" Map the F5 key to run a Python script inside Vim.
" We map F5 to a chain of commands here.
" :w saves the file.
" <CR> (carriage return) is like pressing the enter key.
" !clear runs the external clear screen command.
" !python3 % executes the current file with Python.
nnoremap <f5> :w <CR>:!clear <CR>:!python3 % <CR>

" You can split the window in Vim by typing :split or :vsplit.
" Navigate the split view easier by pressing CTRL+j, CTRL+k, CTRL+h, or CTRL+l.
nnoremap <c-j> <c-w>j
nnoremap <c-k> <c-w>k
nnoremap <c-h> <c-w>h
nnoremap <c-l> <c-w>l

" Resize split windows by pressing:
noremap K <c-w>+
noremap J <c-w>-
noremap L <c-w>>
noremap H <c-w><

" NERDTree specific mappings.
" Map the keys to manipulate NERDTree
nnoremap <leader>n :NERDTreeFocus<CR>
nnoremap <C-n> :NERDTree<CR>
nnoremap <C-t> :NERDTreeToggle<CR>
nnoremap <C-f> :NERDTreeFind<CR>

" Have nerdtree ignore certain files and directories.
let NERDTreeIgnore=['\.git$', '\.jpg$', '\.mp4$', '\.ogg$', '\.iso$', '\.pdf$', '\.pyc$', '\.odt$', '\.png$', '\.gif$', '\.db$']

vnoremap <C-c> :'<,'>w !xclip -selection clipboard<CR><CR>

" FOR ORGANIZING TABS ---{{{
" Move to previous/next
nnoremap <silent>    <A-,> :bprevious<CR>
nnoremap <silent>    <A-.> :bnext<CR>
" Re-order to previous/next
" Goto buffer in position...
nnoremap <silent>    <A-<> :b 1<CR>
nnoremap <silent>    <A-2> :b 2<CR>
nnoremap <silent>    <A-3> :b 3<CR>
nnoremap <silent>    <A-4> :b 4<CR>
nnoremap <silent>    <A-5> :b 5<CR>
nnoremap <silent>    <A-6> :b 6<CR>
nnoremap <silent>    <A-7> :b 7<CR>
nnoremap <silent>    <A-8> :b 8<CR>
nnoremap <silent>    <A-9> :b 9<CR>
nnoremap <silent>    <A->> :blast<CR>
" Pin/unpin buffer
"                          :BufferCloseBuffersRight<CR>
" Magic buffer-picking mode
nnoremap <silent>    <A-c> :bdelete!<CR>
" }}}

" AUTO CLOSING QUOTES AND BRACES ---{{{
inoremap " ""<left>
inoremap ' ''<left>
inoremap ( ()<left>
inoremap [ []<left>
inoremap { {}<left>
"inoremap {<CR> {<CR>}<ESC>O
"inoremap {;<CR> {<CR>};<ESC>O
" }}}

" }}}

" VIMSCRIPT -------------------------------------------------------------- {{{

" Enable the marker method of folding.
augroup filetype_vim
    autocmd!
    autocmd FileType vim setlocal foldmethod=marker
augroup END

" If the current file type is HTML, set indentation to 2 spaces.
autocmd Filetype html setlocal tabstop=2 shiftwidth=2 expandtab

" If Vim version is equal to or greater than 7.3 enable undofile.
" This allows you to undo changes to a file even after saving it.
if version >= 703
    set undodir=~/.vim/backup
    set undofile
    set undoreload=10000
endif

" You can split a window into sections by typing `:split` or `:vsplit`.
" Display cursorline and cursorcolumn ONLY in active window.
augroup cursor_off
    autocmd!
    autocmd WinLeave * set nocursorline nocursorcolumn
    autocmd WinEnter * set cursorline nocursorcolumn
augroup END

" Set the background tone.
set background=dark

" Set a custom font you have installed on your computer.
" Syntax: <font_name>\ <weight>\ <size>
set guifont=Hack\ Regular\ 15

" Display more of the file by default.
" Hide the toolbar.
set guioptions-=T

" Hide the the left-side scroll bar.
set guioptions-=L

" Hide the the left-side scroll bar.
set guioptions-=r

" Hide the the menu bar.
set guioptions-=m

" Hide the the bottom scroll bar.
set guioptions-=b

" Map the F4 key to toggle the menu, toolbar, and scroll bar.
" <Bar> is the pipe character.
" <CR> is the enter key.
nnoremap <F4> :if &guioptions=~#'mTr'<Bar>
    \set guioptions-=mTr<Bar>
    \else<Bar>
    \set guioptions+=mTr<Bar>
    \endif<CR>

" }}}

" STATUS LINE ------------------------------------------------------------ {{{

" Clear status line when vimrc is reloaded.
set statusline=

" Status line left side.
set statusline+=\ %F\ %M\ %Y\ %R

" Use a divider to separate the left side from the right side.
set statusline+=%=

" Status line right side.
"set statusline+=\ ascii:\ %b\ hex:\ 0x%B\ row:\ %l\ col:\ %c\ percent:\ %p%%

let g:python_highlight_all = 1
