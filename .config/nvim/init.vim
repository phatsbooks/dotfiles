set runtimepath^=~/.vim runtimepath+=~/.vim/after
let &packpath=&runtimepath
source ~/.vimrc

source ~/.config/nvim/plugins.vim

" Settings for specific plugins
source ~/.config/nvim/plugrcs/vimtexrc.vim
source ~/.config/nvim/plugrcs/airlinerc.vim
source ~/.config/nvim/plugrcs/cocrc.vim
source ~/.config/nvim/plugrcs/vimspectorrc.vim
source ~/.config/nvim/plugrcs/cppman.vim
source ~/.config/nvim/plugrcs/treesitterrc.vim
source ~/.config/nvim/plugrcs/pyhighlight.vim
source ~/.config/nvim/plugrcs/telescoperc.vim

" Set preferred colorscheme
colorscheme moonlight

let g:indentLine_char='│'

let g:rainbow_active = 1

let g:user_emmet_settings = {
\  'javascript' : {
\      'extends' : 'jsx',
\  },
\}

let g:coc_global_extensions = [
\ 'coc-prettier',
\ 'coc-pairs',
\ 'coc-tsserver',
\ 'coc-json',
\ 'coc-pyright',
\ 'coc-css',
\ 'coc-clangd',
\ 'coc-snippets',
\ 'coc-emmet',
\ 'es7-react-js-snippets'
\ ]

