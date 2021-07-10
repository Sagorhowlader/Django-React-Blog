import React, { useEffect, Fragment } from 'react';
import Navbar from '../components/Navbar';
import { connect } from 'react-redux';
import { checkAuthenticated } from '../actions/auth';
import { load_user } from '../actions/profile';
import { load_Post } from '../actions/post';

const Layout = ({ children, checkAuthenticated, load_user , load_Post }) => {
    useEffect(() => {
        checkAuthenticated();
        load_user();
        load_Post();
    }, []);

    return (
        <Fragment>
            <Navbar />
            {children}
        </Fragment>
    );
};

export default connect(null, { checkAuthenticated, load_user , load_Post })(Layout);
