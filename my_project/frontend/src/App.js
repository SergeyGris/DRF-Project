import React from 'react';
import logo from './logo.svg';
import './App.css';
import UserList from "./components/User";
import axios from 'axios';

class App extends React.Component {
    constructor(props) {
        super(props)
        this.state = {
            'users': []
        }
    }

    componentDidMount() {
        axios.get('http://127.0.0.1:8000/api/users')
            .then(response => {
                const users = response.data
                this.setState({
                    'users': users
                })
            }).catch(error => console.log(error))


    }

    render() {
        return (
            <div>
                <menu>
                    <li>
                        <a href="#">Главная</a>
                    </li>
                    <li>
                        <a href="#">Список пользователей</a>
                    </li>
                </menu>

                <UserList users={this.state.users}/>
                <footer>
                    Lorem ipsum dolor sit.
                </footer>
            </div>
        )
    }
}


export default App;
