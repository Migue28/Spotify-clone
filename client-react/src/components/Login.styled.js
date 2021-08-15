import styled from 'styled-components';
import spotify_logo from '../assets/images/Spotify_Logo_RGB_White.png'

const LoginContainer = styled.div`
    color: white;
    display: flex;
    align-items: center;
    height: 100vh;
    justify-content: center;
    font-family: rubyk, sans-serif;
`

const BlackContainer = styled.div`
    display: grid;
    grid-template-columns: repeat(1, minmax(0, 1fr));
    grid-template-rows: repeat(4, minmax(0, 1fr));
    align-items: center;
    justify-items: center;
    background-color: #191414;
    border-radius: 0.5rem;
    width: 50%;
    height: 50%;
`

const LoginButton = styled.button`
    color: white;
    display: flex;
    align-items: center;
    justify-content: center;
    background-color: #1f9c4b;
    border-radius: 9999px;
    width: 50%;
    height: 50%;
    border: none;
    font-weight: 700;
    &:hover {
        background-color: #1db954;
        transform: scale(1.1);
    } 
`
const Logo = styled.img`
    width: 20%;
    height: auto;
`

const Content = styled.p`
    text-align: center;
    font-size: 1.875rem;
    line-height: 2.25rem;
    font-weight: 200;
`

const Pre = styled.pre`
    color: #e8e8e8;
    font-weight: 200;
`

const A = styled.a`
    color: white;
`

const Login = () => {
    return(
    <LoginContainer>
        <BlackContainer>
            <Logo src={spotify_logo} alt="Spotify logo white"></Logo>
            <Content>Millions of songs.<br />Free on Spotify.</Content>
            <LoginButton>
                LOG IN
            </LoginButton>                
            <Pre>Don't have an account? <A href="/">SIGNUP</A></Pre>
                
        </BlackContainer>
    </LoginContainer>
    )
}

export default Login;