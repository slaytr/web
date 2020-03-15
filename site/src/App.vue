<template>
    <div id="app">
        <header class="body-header">
            <div class="body-logo">
                <router-link to="/">
                    <img class="body-header-logo" src="@/assets/icon.svg" alt="logo"/>
                </router-link>
                <div class="body-header-text-logo">Bill Li</div>
            </div>
            <div id="nav">
                <router-link to="/">
                    <div class="nav-item">
                        Home
                    </div>
                </router-link>
                <router-link to="/about">
                    <div class="nav-item">
                        About
                    </div>
                </router-link>
                <router-link to="/development">
                    <div class="nav-item">
                        Development
                    </div>
                </router-link>
            </div>
        </header>
        <router-view/>
    </div>
</template>

<style lang="scss">
    $white: #FAFAFA;
    $titles: #2C3438;

    body {
        margin: 0;
    }

    .body-logo {
        display: flex;
        flex-direction: row;
        justify-content: center;
        align-items: center;
    }

    .body-header {
        height: 60px;
        background-color: $white;
        box-shadow: 0 1px 1px rgba(0, 0, 0, 0.25);
        display: flex;
        flex-direction: row;
        align-items: center;
    }

    .body-header-logo {
        width: 60px;
        height: 60px;
        opacity: 0.9;
        margin: 0 10px;

        &:hover {
            cursor: pointer;
        }
    }

    .body-header-text-logo {
        font-family: "Roboto";
        font-size: 28px;
        color: $titles;
    }

    #app {
        font-family: Avenir, Helvetica, Arial, sans-serif;
        -webkit-font-smoothing: antialiased;
        -moz-osx-font-smoothing: grayscale;
        text-align: center;
        color: $titles;
    }

    #nav {
        display: flex;
        flex-direction: row;
        align-items: center;
        padding: 30px;

        a {
            text-decoration: none;
            font-weight: bold;
            color: #2c3e50;

            &.router-link-exact-active {
                color: #42b983;
            }
        }
    }

    .nav-item {
        padding: 12px 14px;
        border-radius: 3px;
        transition: background-color 0.5s, color 0.2s;
        margin: 0 2px;

        &:hover {
            background-color: #42b983;
            color: #FAFAFA;
        }
    }
</style>
