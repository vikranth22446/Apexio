import React, {Component} from 'react';
import '../../assets/main.css'

class Header extends Component {
    render() {
        return (
            <div id={"header"}>
                Apexio
            </div>
        );
    }
}

class App extends Component {
    constructor(props) {
        super(props);
        this.state = {
            loading: true
        }
    }

    componentDidMount() {
        setTimeout(this.changeLoading, 3000);
    }

    changeLoading = () => {
        this.setState({loading: false});
    };


    render() {
        let animatedDiv = <div key="loading" id={"mainLogoLoading"} className={"animated animatedFadeInUp fadeInUp"}>
            <img src={"/static/logo.png"} alt={""}/> <br/>
            <em>Declutter your life</em>
        </div>;

        if (!this.state.loading) {
            animatedDiv = <div key="mainDiv" className={"animated animatedFadeInUp fadeInUp"}>
                <div id={"welcomeAnimation"}>Welcome to
                    <br/> <span id={"welcomeSpan"}>Apexio</span>
                </div>

                <div className="parent">
                    <div className="left"><img className="miniLogo" src={"/static/folders.png"}/></div>
                    <div className="right">
                        <span className={"miniLogoTitle"}>Easy organization</span>
                        <br/> Quick AI powered organization
                    </div>
                </div>
                <br/>
                <div className="parent">
                    <div className="left"><img className="miniLogo" src={"/static/privacy.png"} alt={""}/></div>
                    <div className="right">
                        <span className={"miniLogoTitle"}>Secure and private </span>
                        <br/> Everything is offline and encrypted
                    </div>
                </div>
                <br/>
                <div className="parent">
                    <div className="left"><img className="miniLogo" src={"/static/configurable.png"} alt={""}/></div>
                    <div className="right">
                        <span className={"miniLogoTitle"}>Configurability and Control</span> <br/> Specify rules
                        manually or Automatically
                    </div>
                </div>
                <button className={"mainButtonStyle"}>
                    Continue&nbsp;&nbsp;
                    <i className="fa fa-arrow-right rightArrow"/>
                </button>
            </div>;
        }

        return (
            <div>
                <Header/>
                {animatedDiv}
            </div>
        );
    }
}

export default App;