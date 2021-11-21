call plug#begin('~/.vim/plugged')

    Plug 'dense-analysis/ale'
    Plug 'preservim/nerdtree'
    Plug 'Brettm12345/moonlight.vim'
    Plug 'vim-airline/vim-airline'
    Plug 'vim-airline/vim-airline-themes'
    Plug 'neoclide/coc.nvim', {'branch': 'release'}
    Plug 'iamcco/markdown-preview.nvim', { 'do': 'cd app && yarn install'  }
    Plug 'lilydjwg/colorizer'
    Plug 'tpope/vim-commentary'
    Plug 'ryanoasis/vim-devicons'
    Plug 'kyazdani42/nvim-web-devicons'
    Plug 'tiagofumo/vim-nerdtree-syntax-highlight'
    "Plug 'romgrk/barbar.nvim'
    Plug 'mattn/emmet-vim'
    Plug 'lervag/vimtex'
    Plug 'github/copilot.vim'
    Plug 'puremourning/vimspector'
    Plug 'turbio/bracey.vim'
    Plug 'nvim-treesitter/nvim-treesitter', {'do': ':TSUpdate'}  " We recommend updating the parsers on update
    Plug 'dsznajder/vscode-es7-javascript-react-snippets', { 'do': 'yarn install --frozen-lockfile && yarn compile' }
    Plug 'tpope/vim-surround'
    Plug 'bfrg/vim-cpp-modern'
    Plug 'vim-python/python-syntax'
    Plug 'junegunn/goyo.vim'
    Plug 'Yggdroot/indentLine'
    Plug 'nvim-lua/plenary.nvim'
    Plug 'nvim-telescope/telescope.nvim'
    " Plug 'luochen1990/rainbow'

call plug#end()
