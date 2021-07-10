import React from 'react';
import { Link } from 'react-router-dom';
import { connect } from 'react-redux'

const home = ( {isAuthenticated , postList } ) => {
    console.log("post")
    console.log(postList)
    const post = (
        <div className="card" style="width: 18rem;">
                    <img src="..." className="card-img-top" alt="..."/>
                    <div className="card-body">
                        <h5 className="card-title">Card title</h5>
                        <p className="card-text">Some quick example text to build on the card title and make up the bulk of the card's content.</p>
                    </div>
                    <ul className="list-group list-group-flush">
                        <li className="list-group-item">An item</li>
                        <li className="list-group-item">A second item</li>
                        <li className="list-group-item">A third item</li>
                    </ul>
                    <div className="card-body">
                        <a href="#" className="card-link">Card link</a>
                        <a href="#" className="card-link">Another link</a>
                    </div>
    
                </div>
    );
    const beforLogin = (
    <div className='container'>
        <div className='mt-5 p-5 bg-light'>
            <h1 className='display-4'>Welcome to Blog</h1>
            <p className='lead'>
                This is a wonderful application with session authentication in React and Django.
            </p>
            <hr className='my-4' />
            <p>Click the button below to log in.</p>
            <Link className='btn btn-primary btn-lg' to='/login'>Login</Link>
        </div>
    </div>
    );
    const afterLogin = (
    
        <div>post</div>

    
    
        );
    return (
    
    <div> { isAuthenticated ? afterLogin : beforLogin }</div>
    
    );


    };
    const mapStateToProps = state => ({
        isAuthenticated: state.auth.isAuthenticated,
        postList: state.post.userPostsList

    });
export default connect (mapStateToProps)(home);
